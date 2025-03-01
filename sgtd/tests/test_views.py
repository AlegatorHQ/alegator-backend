from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from users.tests.factories import UserFactory, AdminUserFactory
from .factories import (
    SpeakersFactory,
    TeamsFactory,
    AdjudicatorsFactory,
    RoundsFactory,
    DrawsFactory,
    DrawsAdjudicatorsFactory,
    TeamResultsFactory,
    SpeakerResultsFactory,
)
from ..serializers import (
    AdjudicatorsSerializer,
    DrawsSerializer,
    DrawsAdjudicatorsSerializer,
    RoundsSerializer,
    SpeakerResultsSerializer,
    SpeakersSerializer,
    TeamResultsSerializer,
    TeamsSerializer,
)


class TestAdjudicators(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = AdjudicatorsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Adjudicators instances"""

        resp = self.client.get("/api/v1/sgtd/adjudicators/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Adjudicators collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/adjudicators/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that Adjudicators collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/sgtd/adjudicators/",
            {
                "name__icontains": self.instance.name,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Adjudicators instances"""

        resp = self.client.get(f"/api/v1/sgtd/adjudicators/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Adjudicators can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/adjudicators/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Adjudicators"""

        resp = self.client.post("/api/v1/sgtd/adjudicators/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.AdjudicatorsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Adjudicators"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = AdjudicatorsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/adjudicators/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Adjudicators"""

        resp = self.client.patch(f"/api/v1/sgtd/adjudicators/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Adjudicators update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/adjudicators/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Adjudicators"""

        resp = self.client.delete(f"/api/v1/sgtd/adjudicators/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Adjudicators deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/adjudicators/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestDraws(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = DrawsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Draws instances"""

        resp = self.client.get("/api/v1/sgtd/draws/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Draws collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/draws/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Draws instances"""

        resp = self.client.get(f"/api/v1/sgtd/draws/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Draws can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/draws/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Draws"""

        resp = self.client.post("/api/v1/sgtd/draws/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.DrawsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Draws"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = DrawsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/draws/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Draws"""

        resp = self.client.patch(f"/api/v1/sgtd/draws/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Draws update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/draws/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Draws"""

        resp = self.client.delete(f"/api/v1/sgtd/draws/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Draws deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/draws/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestDrawsAdjudicators(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = DrawsAdjudicatorsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list DrawsAdjudicators instances"""

        resp = self.client.get("/api/v1/sgtd/draws-adjudicators/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that DrawsAdjudicators collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/draws-adjudicators/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve DrawsAdjudicators instances"""

        resp = self.client.get(f"/api/v1/sgtd/draws-adjudicators/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of DrawsAdjudicators can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/draws-adjudicators/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new DrawsAdjudicators"""

        resp = self.client.post("/api/v1/sgtd/draws-adjudicators/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.DrawsAdjudicatorsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for DrawsAdjudicators"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = DrawsAdjudicatorsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/draws-adjudicators/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing DrawsAdjudicators"""

        resp = self.client.patch(
            f"/api/v1/sgtd/draws-adjudicators/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test DrawsAdjudicators update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(
            f"/api/v1/sgtd/draws-adjudicators/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete DrawsAdjudicators"""

        resp = self.client.delete(
            f"/api/v1/sgtd/draws-adjudicators/{self.instance.id}/"
        )
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test DrawsAdjudicators deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(
            f"/api/v1/sgtd/draws-adjudicators/{self.instance.id}/"
        )

        self.assertEqual(resp.status_code, 204)


class TestRounds(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = RoundsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Rounds instances"""

        resp = self.client.get("/api/v1/sgtd/rounds/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Rounds collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/rounds/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Rounds instances"""

        resp = self.client.get(f"/api/v1/sgtd/rounds/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Rounds can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/rounds/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Rounds"""

        resp = self.client.post("/api/v1/sgtd/rounds/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.RoundsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Rounds"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = RoundsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/rounds/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Rounds"""

        resp = self.client.patch(f"/api/v1/sgtd/rounds/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Rounds update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/rounds/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Rounds"""

        resp = self.client.delete(f"/api/v1/sgtd/rounds/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Rounds deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/rounds/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestSpeakerResults(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = SpeakerResultsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list SpeakerResults instances"""

        resp = self.client.get("/api/v1/sgtd/speaker-results/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that SpeakerResults collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/speaker-results/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve SpeakerResults instances"""

        resp = self.client.get(f"/api/v1/sgtd/speaker-results/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of SpeakerResults can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/speaker-results/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new SpeakerResults"""

        resp = self.client.post("/api/v1/sgtd/speaker-results/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.SpeakerResultsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for SpeakerResults"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = SpeakerResultsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/speaker-results/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing SpeakerResults"""

        resp = self.client.patch(
            f"/api/v1/sgtd/speaker-results/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test SpeakerResults update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(
            f"/api/v1/sgtd/speaker-results/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete SpeakerResults"""

        resp = self.client.delete(f"/api/v1/sgtd/speaker-results/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test SpeakerResults deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/speaker-results/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestSpeakers(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = SpeakersFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Speakers instances"""

        resp = self.client.get("/api/v1/sgtd/speakers/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Speakers collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/speakers/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Speakers instances"""

        resp = self.client.get(f"/api/v1/sgtd/speakers/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Speakers can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/speakers/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Speakers"""

        resp = self.client.post("/api/v1/sgtd/speakers/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.SpeakersViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Speakers"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = SpeakersSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/speakers/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Speakers"""

        resp = self.client.patch(f"/api/v1/sgtd/speakers/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Speakers update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/speakers/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Speakers"""

        resp = self.client.delete(f"/api/v1/sgtd/speakers/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Speakers deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/speakers/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestTeamResults(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = TeamResultsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list TeamResults instances"""

        resp = self.client.get("/api/v1/sgtd/team-results/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that TeamResults collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/team-results/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve TeamResults instances"""

        resp = self.client.get(f"/api/v1/sgtd/team-results/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of TeamResults can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/team-results/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new TeamResults"""

        resp = self.client.post("/api/v1/sgtd/team-results/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.TeamResultsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for TeamResults"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = TeamResultsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/team-results/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing TeamResults"""

        resp = self.client.patch(f"/api/v1/sgtd/team-results/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test TeamResults update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/team-results/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete TeamResults"""

        resp = self.client.delete(f"/api/v1/sgtd/team-results/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test TeamResults deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/team-results/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestTeams(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = TeamsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Teams instances"""

        resp = self.client.get("/api/v1/sgtd/teams/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Teams collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/teams/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that Teams collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/sgtd/teams/",
            {
                "name__icontains": self.instance.name,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Teams instances"""

        resp = self.client.get(f"/api/v1/sgtd/teams/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Teams can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/teams/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Teams"""

        resp = self.client.post("/api/v1/sgtd/teams/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.TeamsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Teams"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = TeamsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/teams/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Teams"""

        resp = self.client.patch(f"/api/v1/sgtd/teams/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Teams update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/teams/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Teams"""

        resp = self.client.delete(f"/api/v1/sgtd/teams/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Teams deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/teams/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
