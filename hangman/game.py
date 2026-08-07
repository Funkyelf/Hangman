"""
Core Hangman game engine.
"""

from word_manager import WordManager
from achievements import AchievementManager
from statistics import Statistics
from constants import (
    DIFFICULTIES,
    POINTS_CORRECT_LETTER,
    POINTS_WRONG_LETTER,
    POINTS_HINT,
    POINTS_WIN,
    POINTS_LOSS,
    POINTS_WORD_BONUS,
)


class HangmanGame:

    def __init__(self, player, difficulty="medium", category=None):

        self.player = player
        self.difficulty = difficulty

        self.word_manager = WordManager()

        self.word = self.word_manager.choose_word(
            difficulty,
            category
        )

        self.category = self.word.category

        self.lives = DIFFICULTIES[difficulty]["lives"]

        self.guessed_letters = set()

        self.wrong_letters = set()

        self.wrong_guesses = 0

        self.used_hint = False

        self.current_score = 0

        self.finished = False

        self.won = False

        self.statistics = Statistics()

        self.achievement_manager = AchievementManager()

    # -------------------------------------------------

    @property
    def display_word(self):

        return " ".join(

            letter

            if letter in self.guessed_letters

            else "_"

            for letter in self.word.value

        )

    # -------------------------------------------------

    @property
    def remaining_lives(self):

        return self.lives - self.wrong_guesses

    # -------------------------------------------------

    @property
    def solved(self):

        return all(

            letter in self.guessed_letters

            for letter in self.word.value

        )

    # -------------------------------------------------

    def reveal_hint(self):

        if self.used_hint:

            return None

        self.used_hint = True

        self.current_score += POINTS_HINT

        return self.word.hint

    # -------------------------------------------------

    def guess_letter(self, letter):

        letter = letter.lower()

        if self.finished:

            return False, "Game already finished."

        if len(letter) != 1:

            return False, "Enter one letter."

        if not letter.isalpha():

            return False, "Letters only."

        if letter in self.guessed_letters:

            return False, "Already guessed."

        if letter in self.wrong_letters:

            return False, "Already guessed."

        if letter in self.word.value:

            self.guessed_letters.add(letter)

            self.current_score += POINTS_CORRECT_LETTER

            self.statistics.add_letter_guess()

            if self.solved:

                self.win()

            return True, "Correct!"

        self.wrong_letters.add(letter)

        self.wrong_guesses += 1

        self.current_score += POINTS_WRONG_LETTER

        self.statistics.add_letter_guess()

        if self.remaining_lives <= 0:

            self.lose()

        return False, "Wrong!"

    # -------------------------------------------------

    def guess_word(self, guess):

        if self.finished:

            return False, "Game already finished."

        guess = guess.lower().strip()

        if guess == self.word.value:

            self.guessed_letters.update(self.word.value)

            self.current_score += POINTS_WORD_BONUS

            self.win()

            return True, "Correct word!"

        self.wrong_guesses += 1

        self.current_score += POINTS_WRONG_LETTER

        if self.remaining_lives <= 0:

            self.lose()

        return False, "Incorrect word."

    # -------------------------------------------------

    def win(self):

        if self.finished:
            return

        self.finished = True

        self.won = True

        multiplier = DIFFICULTIES[self.difficulty]["multiplier"]

        self.current_score += POINTS_WIN * multiplier

        self.player.add_score(self.current_score)

        self.player.guessed_word()

        self.player.win()

        self.statistics.record_game(
            True,
            self.current_score
        )

        self.achievement_manager.check(
            self.player,
            self.difficulty,
            self.used_hint,
            self.wrong_guesses
        )

    # -------------------------------------------------

    def lose(self):

        if self.finished:
            return

        self.finished = True

        self.current_score += POINTS_LOSS

        self.player.add_score(self.current_score)

        self.player.lose()

        self.statistics.record_game(
            False,
            self.current_score
        )

    # -------------------------------------------------

    def game_state(self):

        return {

            "word": self.display_word,

            "category": self.category,

            "lives": self.remaining_lives,

            "score": self.current_score,

            "wrong": sorted(self.wrong_letters),

            "finished": self.finished,

            "won": self.won,

        }