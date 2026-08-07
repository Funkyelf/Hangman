"""
Player profile management.
"""


from dataclasses import dataclass, field



@dataclass
class Player:


    name: str


    score: int = 0


    games_played: int = 0


    wins: int = 0


    losses: int = 0


    words_guessed: int = 0


    achievements: list = field(
        default_factory=list
    )



    def add_score(
        self,
        amount
    ):

        self.score += amount



    def win(self):

        self.games_played += 1

        self.wins += 1



    def lose(self):

        self.games_played += 1

        self.losses += 1



    def guessed_word(self):

        self.words_guessed += 1



    def unlock(
        self,
        achievement
    ):

        if achievement not in self.achievements:

            self.achievements.append(
                achievement
            )



    def to_dict(self):

        return {

            "name": self.name,

            "score": self.score,

            "games_played":
                self.games_played,

            "wins":
                self.wins,

            "losses":
                self.losses,

            "words_guessed":
                self.words_guessed,

            "achievements":
                self.achievements

        }



    @staticmethod
    def from_dict(data):

        return Player(

            name=data["name"],

            score=data.get(
                "score",
                0
            ),

            games_played=data.get(
                "games_played",
                0
            ),

            wins=data.get(
                "wins",
                0
            ),

            losses=data.get(
                "losses",
                0
            ),

            words_guessed=data.get(
                "words_guessed",
                0
            ),

            achievements=data.get(
                "achievements",
                []
            )

        )