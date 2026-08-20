"""
Profile game statistics.
"""


class Statistics:

    def __init__(self, player):
        self.player = player

    def add_letter_guess(self):
        self.player.guessed_letter()

    def win_rate(self):

        games = self.player.games_played

        if games == 0:
            return 0

        return round(
            (self.player.wins / games) * 100,
            2
        )

    def data(self):

        return {
            "name": self.player.name,
            "score": self.player.score,
            "games played": self.player.games_played,
            "wins": self.player.wins,
            "losses": self.player.losses,
            "words guessed": self.player.words_guessed,
            "letters guessed": self.player.letters_guessed,
            "win rate": self.win_rate()
        }