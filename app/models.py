from django.db import models


class Users(models.Model):
    first_name = models.TextField(
        null=False,
    )
    last_name = models.TextField(
        null=False,
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
    )
    email = models.EmailField(
        null=False,
        unique=True,
    )
    province = models.TextField(
        null=False,
    )
    is_active = models.BooleanField(
        null=False,
    )
    is_staff = models.BooleanField(
        null=False,
    )
    is_authenticated = models.BooleanField(
        null=False,
    )
    is_superuser = models.BooleanField(
        null=False,
    )

    def __str__(self):
        """String representation of a User instance."""
        return self.first_name

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in between."""
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()


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
    creator = models.ForeignKey(
        "app.Users",
        related_name="tournaments",
        on_delete=models.PROTECT,
        null=False,
    )

    def __str__(self):
        """String representation of a Tournaments instance."""
        return self.name


class Usertournament(models.Model):
    user = models.ForeignKey(
        "app.Users",
        related_name="usertournaments",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="usertournaments",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    role = models.TextField(
        null=False,
        editable=False,
    )

    def __str__(self):
        """String representation of a Usertournament instance."""
        return self.role
