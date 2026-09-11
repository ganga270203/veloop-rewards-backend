from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    reward = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="game_scores"
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="scores"
    )

    score = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    played_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.score}"