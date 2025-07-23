from django.db import models
from django.utils.timezone import now
from django.conf import settings


class Speakers(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="speakers",
        on_delete=models.CASCADE,
        null=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="speakers",
        on_delete=models.CASCADE,
        null=False,
    )
    province = models.TextField(
        null=False,
    )
    delegation = models.TextField(
        null=False,
    )
    is_novice = models.BooleanField(
        null=False,
        default=False,
    )

    def __str__(self):
        """String representation of a Speakers instance."""
        return self.user.first_name


class Teams(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="teams",
        on_delete=models.CASCADE,
        null=False,
    )
    name = models.TextField(
        null=False,
        unique=True,
    )
    speaker_1 = models.ForeignKey(
        "sgtd.Speakers",
        related_name="teams_speaker_1",
        on_delete=models.PROTECT,
        null=False,
    )
    speaker_2 = models.ForeignKey(
        "sgtd.Speakers",
        related_name="teams_speaker_2",
        on_delete=models.PROTECT,
        null=False,
    )

    def __str__(self):
        """String representation of a Teams instance."""
        return self.name


class Judges(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="judges",
        on_delete=models.CASCADE,
        null=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="judges",
        on_delete=models.CASCADE,
        null=False,
    )
    province = models.TextField(
        null=False,
    )
    delegation = models.TextField(
        null=False,
    )
    team = models.ForeignKey(
        "sgtd.Teams",
        related_name="judges",
        on_delete=models.PROTECT,
        null=False,
    )
    basescore = models.DecimalField(
        null=False,
        max_digits=3,
        decimal_places=2,
    )

    def __str__(self):
        """String representation of a Judges instance."""
        return self.user.first_name


class Rounds(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="rounds",
        on_delete=models.CASCADE,
        null=False,
    )
    name = models.TextField(
        null=False,
        unique=True,
    )
    motion = models.TextField(
        null=False,
    )
    infoslide = models.TextField(
        null=False,
    )
    round_number = models.IntegerField(
        null=False,
    )
    round_status = models.TextField(
        null=False,
    )
    round_type = models.BooleanField(
        null=False,
    )
    is_silenced = models.BooleanField(
        null=False,
    )

    def __str__(self):
        """String representation of a Rounds instance."""
        return self.name


class Draws(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="draws",
        on_delete=models.CASCADE,
        null=False,
    )
    round = models.ForeignKey(
        "sgtd.Rounds",
        related_name="draws",
        on_delete=models.PROTECT,
        null=False,
    )
    draw_status = models.TextField(
        null=False,
    )
    ag = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws_ag",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    ao = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws_ao",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    bg = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws_bg",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    bo = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws_bo",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


class Drawsjudges(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="drawsjudges",
        on_delete=models.CASCADE,
        null=False,
    )
    draw = models.ForeignKey(
        "sgtd.Judges",
        related_name="drawsjudges_draw",
        on_delete=models.PROTECT,
        null=False,
    )
    judge = models.ForeignKey(
        "sgtd.Judges",
        related_name="drawsjudges_judge",
        on_delete=models.PROTECT,
        null=False,
    )
    role = models.TextField(
        null=False,
    )
    is_checked = models.BooleanField(
        null=False,
        default=False,
    )


class Teamresults(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="teamresults",
        on_delete=models.CASCADE,
        null=False,
    )
    draw = models.ForeignKey(
        "sgtd.Draws",
        related_name="teamresults",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    team = models.ForeignKey(
        "sgtd.Teams",
        related_name="teamresults",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    position = models.TextField(
        null=False,
    )
    points = models.IntegerField(
        null=False,
    )


class Speakerresults(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="speakerresults",
        on_delete=models.CASCADE,
        null=False,
    )
    draw = models.ForeignKey(
        "sgtd.Draws",
        related_name="speakerresults",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    speaker = models.ForeignKey(
        "sgtd.Speakers",
        related_name="speakerresults",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    speaker_points = models.DecimalField(
        null=False,
        max_digits=3,
        decimal_places=2,
    )
    is_iron = models.BooleanField(
        null=False,
        default=False,
    )
    team_result = models.ForeignKey(
        "sgtd.Teamresults",
        related_name="speakerresults",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )


class Checkins(models.Model):
    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="checkins",
        on_delete=models.CASCADE,
        null=False,
    )
    created_at = models.DateTimeField(
        null=False,
        default=now,
    )
    update_at = models.DateTimeField(
        null=False,
        default=now,
    )
    round = models.ForeignKey(
        "sgtd.Rounds",
        related_name="checkins",
        on_delete=models.CASCADE,
        null=False,
    )
    speaker = models.ForeignKey(
        "sgtd.Speakers",
        related_name="checkins",
        on_delete=models.CASCADE,
        null=False,
    )


class Feedbacks(models.Model):
    FEEDBACK_TYPE_CHOICES = [
        ("speaker_to_judge", "Speaker to Judge"),
        ("judge_to_speaker", "Judge to Speaker"),
    ]

    tournament = models.ForeignKey(
        "app.Tournaments",
        related_name="feedbacks",
        on_delete=models.CASCADE,
        null=False,
    )
    draw = models.ForeignKey(
        "sgtd.Draws",
        related_name="feedbacks",
        on_delete=models.PROTECT,
        null=False,
    )
    feedback_type = models.CharField(
        max_length=20,
        choices=FEEDBACK_TYPE_CHOICES,
        null=False,
    )
    given_by = models.TextField(
        null=False,
    )
    target = models.TextField(
        null=False,
    )
    comment = models.TextField(
        null=False,
    )
    score = models.IntegerField(
        null=False,
    )
    status = models.TextField(
        null=False,
        default="pending",
    )

    def __str__(self):
        feedback_type_value = self.feedback_type
        if isinstance(feedback_type_value, str):
            feedback_type_display = dict(self.FEEDBACK_TYPE_CHOICES).get(
                feedback_type_value, feedback_type_value
            )
        else:
            feedback_type_display = str(feedback_type_value)
        return f"Feedback: {self.given_by} → {self.target} [{feedback_type_display}] | Score: {self.score} | Status: {self.status}"
