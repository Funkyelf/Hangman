"""
Score management system.
"""

from constants import SCORE_FILE
from utils import load_json, save_json


class ScoreManager:


    def __init__(self):

        self.scores = load_json(
            SCORE_FILE,
            []
        )


    def add_score(
        self,
        player
    ):

        entry = {

            "name": player.name,

            "score": player.score,

            "wins": player.wins,

            "games": player.games_played

        }


        self.scores.append(entry)

        self.scores.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        # keep top 100
        self.scores = self.scores[:100]


        self.save()



    def save(self):

        save_json(
            SCORE_FILE,
            self.scores
        )



    def leaderboard(
        self,
        limit=10
    ):

        return self.scores[:limit]