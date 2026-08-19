"""
Achievement system.
"""

import json

from constants import ACHIEVEMENTS, ACHIEVEMENTS_FILE


class AchievementManager:

    def check(
        self,
        player,
        difficulty,
        used_hint,
        mistakes
    ):
        unlocked = []

        # First win
        if (
            player.wins >= 1
            and "first_win" not in player.achievements
        ):
            unlocked.append("first_win")

        # Perfect game
        if (
            mistakes == 0
            and "perfect_game" not in player.achievements
        ):
            unlocked.append("perfect_game")

        # Hard mode
        if (
            difficulty == "hard"
            and "hard_mode" not in player.achievements
        ):
            unlocked.append("hard_mode")

        # No hints
        if (
            not used_hint
            and "no_hints" not in player.achievements
        ):
            unlocked.append("no_hints")

        # Word master
        if (
            player.words_guessed >= 50
            and "word_master" not in player.achievements
        ):
            unlocked.append("word_master")

        for achievement in unlocked:
            player.unlock(achievement)

        self.save(player)

        return unlocked

    def name(self, achievement):
        return ACHIEVEMENTS[achievement]["name"]

    def description(self, achievement):
        return ACHIEVEMENTS[achievement]["description"]

    def save(self, player):
        ACHIEVEMENTS_FILE.parent.mkdir(exist_ok=True)

        # Load existing player achievements
        if ACHIEVEMENTS_FILE.exists():
            with open(ACHIEVEMENTS_FILE, "r") as file:
                all_achievements = json.load(file)
        else:
            all_achievements = {}

        # Save this player's achievements
        all_achievements[player.name] = player.achievements

        with open(ACHIEVEMENTS_FILE, "w") as file:
            json.dump(all_achievements, file, indent=4)


    def load(self, player):
        if not ACHIEVEMENTS_FILE.exists():
            player.achievements = []
            return

        with open(ACHIEVEMENTS_FILE, "r") as file:
            all_achievements = json.load(file)

        # Load this player's achievements
        player.achievements = all_achievements.get(player.name, [])
