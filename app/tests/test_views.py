from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from .factories import (
    TournamentsFactory,
    UsertournamentFactory,
    UserFactory,
    AdminUserFactory,
)
from ..serializers import TournamentsSerializer, UserSerializer


class TestUser(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()

    def test_non_admin_list_fails(self):
        """Test that regular users can't list other users"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/users/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that admins can list users"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.get("/api/v1/users/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 2)

        user_ids = {user["id"] for user in data["results"]}
        self.assertEqual(user_ids, {self.user.id, self.admin.id})

    def test_non_admin_get_fails(self):
        """Test that regular users can't retrieve other user's data"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/users/{self.admin.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get_self(self):
        """Test that users can their own user data"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/users/{self.user.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.user.id)

    def test_get_other(self):
        """Test that admins can get other user's data"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(f"/api/v1/users/{self.user.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.user.id)

    def test_non_admin_create_fails(self):
        """Test that regular users can't create a new user"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.post("/api/v1/users/")
        self.assertEqual(resp.status_code, 403)

    @patch("app.views.UserViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for users.User"""

        self.client.force_authenticate(user=self.admin)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = UserSerializer(self.user).data

        resp = self.client.post("/api/v1/users/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_non_admin_update_fails(self):
        """Test that anonymous users can't update user data"""

        resp = self.client.patch(f"/api/v1/users/{self.user.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test admins can update user data"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/users/{self.user.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_non_admin_delete_fails(self):
        """Test that regular users can't delete users"""

        resp = self.client.delete(f"/api/v1/users/{self.user.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test admins can delete users"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/users/{self.user.id}/")
        self.assertEqual(resp.status_code, 204)


class TestTournaments(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = TournamentsFactory(creator=self.user)

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Tournaments instances"""

        resp = self.client.get("/api/v1/tournaments/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Tournaments collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/tournaments/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Tournaments instances"""

        resp = self.client.get(f"/api/v1/tournaments/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Tournaments can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/tournaments/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Tournaments"""

        resp = self.client.post("/api/v1/tournaments/")
        self.assertEqual(resp.status_code, 403)

    @patch("app.views.TournamentsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Tournaments"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = TournamentsSerializer(self.instance).data

        resp = self.client.post("/api/v1/tournaments/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with(creator=self.user)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Tournaments"""

        resp = self.client.patch(f"/api/v1/tournaments/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Tournaments update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/tournaments/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Tournaments"""

        resp = self.client.delete(f"/api/v1/tournaments/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Tournaments deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/tournaments/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestUsertournament(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = UsertournamentFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Usertournament instances"""

        resp = self.client.get("/api/v1/usertournament/")
        self.assertEqual(resp.status_code, 403)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Usertournament instances"""

        resp = self.client.get(f"/api/v1/usertournament/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Usertournament"""

        resp = self.client.post("/api/v1/usertournament/")
        self.assertEqual(resp.status_code, 403)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Usertournament"""

        resp = self.client.patch(f"/api/v1/usertournament/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Usertournament"""

        resp = self.client.delete(f"/api/v1/usertournament/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)
