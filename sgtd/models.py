from django.db import models
from django.utils.timezone import now


class Speakers(models.Model):
    name = models.TextField(
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
        return self.name


class Teams(models.Model):
    name = models.TextField(
        null=False,
        unique=True,
    )
    speaker_1 = models.ForeignKey(
        "users.User",
        related_name="teams_speaker_1",
        on_delete=models.PROTECT,
        null=False,
    )
    speaker_2 = models.ForeignKey(
        "users.User",
        related_name="teams_speaker_2",
        on_delete=models.PROTECT,
        null=False,
    )
    teamtype = models.TextField(
        null=False,
    )

    def __str__(self):
        """String representation of a Teams instance."""
        return self.name


class Judges(models.Model):
    name = models.TextField(
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
        return self.name


class Rounds(models.Model):
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
        null=False,
    )
    ao = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws_ao",
        on_delete=models.CASCADE,
        null=False,
    )
    bg = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws_bg",
        on_delete=models.CASCADE,
        null=False,
    )
    bo = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws_bo",
        on_delete=models.CASCADE,
        null=False,
    )


class Drawsjudges(models.Model):
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
    draw = models.ForeignKey(
        "sgtd.Draws",
        related_name="teamresults",
        on_delete=models.PROTECT,
        null=False,
    )
    team = models.ForeignKey(
        "sgtd.Teams",
        related_name="teamresults",
        on_delete=models.PROTECT,
        null=False,
    )
    position = models.TextField(
        null=False,
    )
    points = models.IntegerField(
        null=False,
    )


class Speakerresults(models.Model):
    draw = models.ForeignKey(
        "sgtd.Draws",
        related_name="speakerresults",
        on_delete=models.PROTECT,
        null=False,
    )
    speaker = models.ForeignKey(
        "sgtd.Speakers",
        related_name="speakerresults",
        on_delete=models.PROTECT,
        null=False,
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
        null=False,
    )


class Checkins(models.Model):
    created_at = models.DateTimeField(
        null=False,
        default=now,
    )
    update_at = models.DateTimeField(
        null=False,
    )
    round = models.OneToOneField(
        "sgtd.Rounds",
        related_name="checkins",
        on_delete=models.CASCADE,
        null=False,
        unique=True,
    )
    speaker = models.OneToOneField(
        "sgtd.Speakers",
        related_name="checkins",
        on_delete=models.CASCADE,
        null=False,
        unique=True,
    )


class Feedbacks(models.Model):
    FEEDBACK_TYPE_CHOICES = [
        ("speaker_to_judge", "Speaker to Judge"),
        ("judge_to_speaker", "Judge to Speaker"),
    ]

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
        feedback_type_display = dict(self.FEEDBACK_TYPE_CHOICES).get(self.feedback_type, self.feedback_type)
        return f"Feedback: {self.given_by} → {self.target} [{feedback_type_display}] | Score: {self.score} | Status: {self.status}"
