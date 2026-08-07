"""
Achievement system.
"""


from constants import ACHIEVEMENTS



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
            and
            "first_win"
            not in player.achievements

        ):

            unlocked.append(
                "first_win"
            )



        # Perfect game

        if (

            mistakes == 0
            and
            "perfect_game"
            not in player.achievements

        ):

            unlocked.append(
                "perfect_game"
            )



        # Hard mode

        if (

            difficulty == "hard"
            and
            "hard_mode"
            not in player.achievements

        ):

            unlocked.append(
                "hard_mode"
            )



        # No hints

        if (

            not used_hint
            and
            "no_hints"
            not in player.achievements

        ):

            unlocked.append(
                "no_hints"
            )



        # Word master

        if (

            player.words_guessed >= 50

            and

            "word_master"
            not in player.achievements

        ):

            unlocked.append(
                "word_master"
            )



        for achievement in unlocked:

            player.unlock(
                achievement
            )


        return unlocked



    def description(
        self,
        achievement
    ):

        return ACHIEVEMENTS[achievement]