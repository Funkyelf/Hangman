"""
Game save/load system.
"""


from constants import SAVE_FILE
from utils import load_json, save_json



class SaveManager:


    def save_game(
        self,
        game
    ):

        data = {


            "player":
                game.player.to_dict(),


            "word":
                game.word.value,


            "hint":
                game.word.hint,


            "category":
                game.word.category,


            "difficulty":
                game.difficulty,


            "guessed":
                list(game.guessed_letters),


            "wrong":
                game.wrong_guesses,


            "score":
                game.current_score,


            "used_hint":
                game.used_hint

        }


        save_json(
            SAVE_FILE,
            data
        )



    def load_game(self):

        return load_json(
            SAVE_FILE,
            None
        )



    def delete_save(self):

        if SAVE_FILE.exists():

            SAVE_FILE.unlink()