from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from app.tests.factories import UserFactory, AdminUserFactory
from .factories import (
    SpeakersFactory,
    TeamsFactory,
    JudgesFactory,
    RoundsFactory,
    DrawsFactory,
    TeamresultsFactory,
    SpeakerresultsFactory,
    CheckinsFactory,
    FeedbacksFactory,
)
from ..serializers import (
    CheckinsSerializer,
    DrawsSerializer,
    FeedbacksSerializer,
    JudgesSerializer,
    RoundsSerializer,
    SpeakerresultsSerializer,
    SpeakersSerializer,
    TeamresultsSerializer,
    TeamsSerializer,
)


class TestCheckins(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = CheckinsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Checkins instances"""

        resp = self.client.get("/api/v1/sgtd/checkins/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Checkins collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/checkins/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Checkins instances"""

        resp = self.client.get(f"/api/v1/sgtd/checkins/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Checkins can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/checkins/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Checkins"""

        resp = self.client.post("/api/v1/sgtd/checkins/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.CheckinsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Checkins"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = CheckinsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/checkins/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Checkins"""

        resp = self.client.patch(f"/api/v1/sgtd/checkins/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Checkins update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/checkins/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Checkins"""

        resp = self.client.delete(f"/api/v1/sgtd/checkins/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Checkins deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/checkins/{self.instance.id}/")

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


class TestFeedbacks(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = FeedbacksFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Feedbacks instances"""

        resp = self.client.get("/api/v1/sgtd/feedbacks/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Feedbacks collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/feedbacks/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Feedbacks instances"""

        resp = self.client.get(f"/api/v1/sgtd/feedbacks/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Feedbacks can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/feedbacks/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Feedbacks"""

        resp = self.client.post("/api/v1/sgtd/feedbacks/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.FeedbacksViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Feedbacks"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = FeedbacksSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/feedbacks/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Feedbacks"""

        resp = self.client.patch(f"/api/v1/sgtd/feedbacks/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Feedbacks update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/sgtd/feedbacks/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Feedbacks"""

        resp = self.client.delete(f"/api/v1/sgtd/feedbacks/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Feedbacks deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/feedbacks/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestJudges(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = JudgesFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Judges instances"""

        resp = self.client.get("/api/v1/sgtd/judges/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Judges collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/judges/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Judges instances"""

        resp = self.client.get(f"/api/v1/sgtd/judges/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Judges can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/judges/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Judges"""

        resp = self.client.post("/api/v1/sgtd/judges/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.JudgesViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Judges"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = JudgesSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/judges/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Judges"""

        resp = self.client.patch(f"/api/v1/sgtd/judges/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Judges update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/judges/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Judges"""

        resp = self.client.delete(f"/api/v1/sgtd/judges/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Judges deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/judges/{self.instance.id}/")

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


class TestSpeakerresults(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = SpeakerresultsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Speakerresults instances"""

        resp = self.client.get("/api/v1/sgtd/speakerresults/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Speakerresults collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/speakerresults/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Speakerresults instances"""

        resp = self.client.get(f"/api/v1/sgtd/speakerresults/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Speakerresults can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/speakerresults/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Speakerresults"""

        resp = self.client.post("/api/v1/sgtd/speakerresults/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.SpeakerresultsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Speakerresults"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = SpeakerresultsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/speakerresults/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Speakerresults"""

        resp = self.client.patch(f"/api/v1/sgtd/speakerresults/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Speakerresults update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/speakerresults/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Speakerresults"""

        resp = self.client.delete(f"/api/v1/sgtd/speakerresults/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Speakerresults deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/speakerresults/{self.instance.id}/")

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


class TestTeamresults(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = TeamresultsFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Teamresults instances"""

        resp = self.client.get("/api/v1/sgtd/teamresults/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Teamresults collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/sgtd/teamresults/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Teamresults instances"""

        resp = self.client.get(f"/api/v1/sgtd/teamresults/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Teamresults can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/sgtd/teamresults/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Teamresults"""

        resp = self.client.post("/api/v1/sgtd/teamresults/")
        self.assertEqual(resp.status_code, 403)

    @patch("sgtd.views.TeamresultsViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Teamresults"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = TeamresultsSerializer(self.instance).data

        resp = self.client.post("/api/v1/sgtd/teamresults/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Teamresults"""

        resp = self.client.patch(f"/api/v1/sgtd/teamresults/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Teamresults update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/sgtd/teamresults/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Teamresults"""

        resp = self.client.delete(f"/api/v1/sgtd/teamresults/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Teamresults deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/sgtd/teamresults/{self.instance.id}/")

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
