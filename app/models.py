from django.db import models


class Tournaments(models.Model):
    name = models.TextField(
        null=False,
        unique=True,
        verbose_name="tournament name",
    )
    description_tournament = models.TextField(
        null=True,
    )
    tournament_status = models.TextField(
        null=False,
    )
    avoid_same_institution = models.BooleanField(
        null=False,
    )
    shortname = models.TextField(
        null=True,
    )
    place = models.TextField(
        null=True,
    )
    missing_feedbacks = models.BooleanField(
        null=False,
    )
    feedback_description = models.TextField(
        null=True,
    )
    speaker_criteria = models.JSONField(
        null=True,
    )
    minimum_panel_score = models.IntegerField(
        null=False,
    )
    check_in = models.BooleanField(
        null=False,
    )
    start_date = models.DateField(
        null=False,
    )
    end_date = models.DateField(
        null=False,
    )
    team_criteria = models.JSONField(
        null=True,
    )
    creator = models.ForeignKey(
        "users.User",
        related_name="tournaments",
        on_delete=models.PROTECT,
        null=False,
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        null=False,
    )

    def __str__(self):
        """String representation of a Tournaments instance."""
        return self.name


class Usertournament(models.Model):
    user = models.ManyToManyField(
        "users.User",
        related_name="usertournaments",
        blank=True,
        editable=False,
    )
    tournament = models.ManyToManyField(
        "app.Tournaments",
        related_name="usertournaments",
        blank=True,
        editable=False,
    )
    role = models.TextField(
        null=False,
        editable=False,
    )

    def __str__(self):
        """String representation of a Usertournament instance."""
        return self.role
