"""
Word database manager for Hangman.
"""

import random
from dataclasses import dataclass

from constants import WORDS_FILE, DIFFICULTIES


@dataclass
class Word:
    """
    Represents a Hangman word.
    """

    value: str
    hint: str
    category: str


class WordManager:

    def __init__(self):

        self.words = []
        self.load_words()


    def load_words(self):

        """
        Loads words from the word database.
        
        Format:

        word|hint|category

        Example:

        python|Programming language|Technology
        """

        if not WORDS_FILE.exists():

            return


        with open(
            WORDS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue


                try:

                    word, hint, category = line.split("|")

                    self.words.append(
                        Word(
                            word.lower(),
                            hint,
                            category
                        )
                    )

                except ValueError:

                    continue



    def categories(self):

        """
        Returns available categories.
        """

        return sorted(
            set(
                word.category
                for word in self.words
            )
        )


    def get_words_by_category(self, category):

        return [
            word
            for word in self.words
            if word.category == category
        ]



    def get_words_by_difficulty(self, difficulty):

        settings = DIFFICULTIES[difficulty]

        return [

            word

            for word in self.words

            if settings["min_length"]
            <= len(word.value)
            <= settings["max_length"]

        ]



    def choose_word(self, difficulty, category=None):

        possible = self.get_words_by_difficulty(difficulty)


        if category:

            possible = [

                word

                for word in possible

                if word.category == category

            ]


        if not possible:

            raise Exception("No words match the selected options.")


        return random.choice(possible)