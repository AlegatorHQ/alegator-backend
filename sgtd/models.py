from django.db import models


class Speakers(models.Model):
    name = models.TextField(
        null=False,
    )
    province = models.TextField(
        null=False,
    )
    nickname = models.TextField(
        null=False,
        unique=True,
    )
    status = models.BooleanField(
        null=False,
    )
    institution = models.TextField(
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

    def __str__(self):
        """String representation of a Teams instance."""
        return self.name


class Adjudicators(models.Model):
    name = models.TextField(
        null=False,
    )
    province = models.TextField(
        null=False,
    )
    institution = models.TextField(
        null=False,
    )
    team_representation = models.ForeignKey(
        "sgtd.Teams",
        related_name="adjudicators",
        on_delete=models.PROTECT,
        null=False,
    )
    score = models.DecimalField(
        null=False,
        max_digits=3,
        decimal_places=2,
    )

    def __str__(self):
        """String representation of a Adjudicators instance."""
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
    speaker_position = models.ForeignKey(
        "sgtd.Speakers",
        related_name="draws",
        on_delete=models.PROTECT,
        null=False,
    )
    adjudicator = models.ForeignKey(
        "sgtd.Adjudicators",
        related_name="draws",
        on_delete=models.PROTECT,
        null=False,
    )
    draw_status = models.TextField(
        null=False,
    )


class DrawsAdjudicators(models.Model):
    draw = models.ForeignKey(
        "sgtd.Adjudicators",
        related_name="draws_adjudicators_draw",
        on_delete=models.PROTECT,
        null=False,
    )
    adjudicator = models.ForeignKey(
        "sgtd.Adjudicators",
        related_name="draws_adjudicators_adjudicator",
        on_delete=models.PROTECT,
        null=False,
    )
    role = models.TextField(
        null=False,
    )


class TeamResults(models.Model):
    draw = models.ForeignKey(
        "sgtd.Draws",
        related_name="team_results",
        on_delete=models.PROTECT,
        null=False,
    )
    team = models.ForeignKey(
        "sgtd.Teams",
        related_name="team_results",
        on_delete=models.PROTECT,
        null=False,
    )
    position = models.TextField(
        null=False,
    )
    points = models.IntegerField(
        null=False,
    )


class SpeakerResults(models.Model):
    draw = models.ForeignKey(
        "sgtd.Draws",
        related_name="speaker_results",
        on_delete=models.PROTECT,
        null=False,
    )
    speaker = models.ForeignKey(
        "sgtd.Speakers",
        related_name="speaker_results",
        on_delete=models.PROTECT,
        null=False,
    )
    speaker_points = models.DecimalField(
        null=False,
        max_digits=3,
        decimal_places=2,
    )
