from django.core.management.base import BaseCommand
from games.models import Game


class Command(BaseCommand):
    help = "Seed the 13 VELOOP Rewards games"

    def handle(self, *args, **options):

        games = [
            {
                "name": "Reaction Game",
                "slug": "reaction-game",
                "description": "Tap the target as quickly as possible and earn coins.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Memory Match",
                "slug": "memory-match",
                "description": "Match the correct pairs and test your memory.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Number Rush",
                "slug": "number-rush",
                "description": "Solve number challenges quickly and earn rewards.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Quick Tap",
                "slug": "quick-tap",
                "description": "Tap the targets quickly before the timer runs out.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Color Match",
                "slug": "color-match",
                "description": "Find and match the correct colors to score points.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Word Puzzle",
                "slug": "word-puzzle",
                "description": "Solve word puzzles and challenge your vocabulary.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Bubble Pop",
                "slug": "bubble-pop",
                "description": "Pop as many bubbles as you can and collect coins.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "2048 Challenge",
                "slug": "2048-challenge",
                "description": "Combine matching numbers and reach the highest score.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Speed Quiz",
                "slug": "speed-quiz",
                "description": "Answer questions quickly and earn Game Coins.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Catch It",
                "slug": "catch-it",
                "description": "Catch the falling objects before they disappear.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Block Puzzle",
                "slug": "block-puzzle",
                "description": "Place blocks correctly and complete the puzzle.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Lucky Spin",
                "slug": "lucky-spin",
                "description": "Spin the wheel and try your luck to win coins.",
                "reward": 20,
                "is_active": True,
            },
            {
                "name": "Treasure Hunt",
                "slug": "treasure-hunt",
                "description": "Find hidden treasures and collect exciting rewards.",
                "reward": 20,
                "is_active": True,
            },
        ]

        created = 0

        for data in games:
            game, was_created = Game.objects.get_or_create(
                slug=data["slug"],
                defaults=data
            )

            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Games created: {created}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Total games: {Game.objects.count()}"
            )
        )