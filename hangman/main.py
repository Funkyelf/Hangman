"""
Main entry point.
"""

from player import Player
from game import HangmanGame
from word_manager import WordManager
from ui import TerminalUI
from score_manager import ScoreManager
from save_manager import SaveManager
from statistics import Statistics


def play():

    name = input("Player name: ").strip()

    if not name:
        name = "Player"

    player = Player(name)

    score_manager = ScoreManager()
    save_manager = SaveManager()

    while True:

        choice = TerminalUI.main_menu()

        if choice == "5":
            break

        if choice == "3":

            TerminalUI.leaderboard(
                score_manager.leaderboard()
            )

            continue

        if choice == "4":

            TerminalUI.statistics(
                Statistics().data
            )

            continue

        if choice == "2":

            save = save_manager.load_game()

            if save is None:

                TerminalUI.message(
                    "No saved game found."
                )

                continue

            game = HangmanGame(
                player,
                save["difficulty"]
            )

            game.word.value = save["word"]
            game.word.hint = save["hint"]
            game.word.category = save["category"]

            game.guessed_letters = set(
                save["guessed"]
            )

            game.wrong_guesses = save["wrong"]

            game.current_score = save["score"]

            game.used_hint = save["used_hint"]

        else:

            difficulty = TerminalUI.difficulty_menu()

            wm = WordManager()

            category = TerminalUI.category_menu(
                wm.categories()
            )

            game = HangmanGame(
                player,
                difficulty,
                category
            )

        while not game.finished:

            TerminalUI.display(game)

            command = TerminalUI.ask()

            if not command:
                continue

            if command == "!hint":

                hint = game.reveal_hint()

                if hint:

                    TerminalUI.show_hint(hint)

                else:

                    TerminalUI.message(
                        "Hint already used."
                    )

                continue

            if command == "!save":

                save_manager.save_game(game)

                TerminalUI.message(
                    "Game saved."
                )

                continue

            if command == "!quit":

                save_manager.save_game(game)

                return


            if len(command) == 1:
                game.guess_letter(command)
            else:
                game.guess_word(command)


        TerminalUI.game_over(game)

        score_manager.add_score(player)


if __name__ == "__main__":
    play()