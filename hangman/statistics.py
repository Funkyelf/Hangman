"""
Global game statistics.
"""

from constants import STATS_FILE
from utils import load_json, save_json



class Statistics:


    def __init__(self):

        self.data = load_json(
            STATS_FILE,
            {
                "games": 0,
                "wins": 0,
                "losses": 0,
                "total_score": 0,
                "letters_guessed": 0
            }
        )


    def record_game(
        self,
        win,
        score
    ):

        self.data["games"] += 1


        if win:

            self.data["wins"] += 1

        else:

            self.data["losses"] += 1



        self.data["total_score"] += score


        self.save()



    def add_letter_guess(self):

        self.data["letters_guessed"] += 1



    def win_rate(self):

        games = self.data["games"]

        if games == 0:

            return 0


        return round(
            (
                self.data["wins"]
                /
                games
            )
            *
            100,
            2
        )



    def save(self):

        save_json(
            STATS_FILE,
            self.data
        )