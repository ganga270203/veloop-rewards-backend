from rest_framework import serializers
from .models import Game, Score


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    game_name = serializers.CharField(
        source="game.name",
        read_only=True
    )

    class Meta:
        model = Score
        fields = [
            "id",
            "game",
            "game_name",
            "score",
            "coins",
            "played_at",
        ]

        read_only_fields = [
            "id",
            "game_name",
            "played_at",
        ]