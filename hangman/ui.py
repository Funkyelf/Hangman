"""
Terminal user interface for Hangman.
"""

from constants import (
    Colors,
    DIFFICULTIES,
    HANGMAN,
)

from utils import (
    clear_screen,
    pause,
)


class TerminalUI:

    @staticmethod
    def banner():

        print(
            Colors.CYAN
            + Colors.BOLD
            + "=" * 55
        )

        print("                HANGMAN")

        print("=" * 55 + Colors.RESET)

    # ------------------------------------------------

    @staticmethod
    def main_menu():

        clear_screen()

        TerminalUI.banner()

        print("1) New Game")
        print("2) Resume Saved Game")
        print("3) High Scores")
        print("4) Statistics")
        print("5) Quit")

        while True:

            choice = input("\nChoice: ").strip()

            if choice in {"1", "2", "3", "4", "5"}:
                return choice

            print("Invalid selection.")

    # ------------------------------------------------

    @staticmethod
    def difficulty_menu():

        clear_screen()

        TerminalUI.banner()

        print("Choose Difficulty\n")

        print("1) Easy")
        print("2) Medium")
        print("3) Hard")

        while True:

            choice = input("\nChoice: ").strip()

            if choice == "1":
                return "easy"

            if choice == "2":
                return "medium"

            if choice == "3":
                return "hard"

            print("Invalid selection.")

    # ------------------------------------------------

    @staticmethod
    def category_menu(categories):

        clear_screen()

        TerminalUI.banner()

        print("Categories\n")

        print("0) Random")

        for i, category in enumerate(categories, start=1):

            print(f"{i}) {category}")

        while True:

            choice = input("\nChoice: ").strip()

            if choice == "0":
                return None

            if choice.isdigit():

                index = int(choice) - 1

                if 0 <= index < len(categories):
                    return categories[index]

            print("Invalid selection.")

    # ------------------------------------------------

    @staticmethod
    def display(game):

        clear_screen()

        TerminalUI.banner()

        print(HANGMAN[game.wrong_guesses])

        print(f"Difficulty : {DIFFICULTIES[game.difficulty]['name']}")
        print(f"Category   : {game.category}")
        print(f"Lives      : {game.remaining_lives}")
        print(f"Score      : {game.current_score}")

        print()

        print(
            Colors.BOLD
            + game.display_word
            + Colors.RESET
        )

        print()

        if game.wrong_letters:

            print(
                "Wrong letters:",
                ", ".join(sorted(game.wrong_letters))
            )

        print()

        print("Commands")
        print("---------------------")
        print("letter")
        print("!hint")
        print("!save")
        print("!quit")

    # ------------------------------------------------

    @staticmethod
    def ask():

        return input("\n> ").strip()

    # ------------------------------------------------

    @staticmethod
    def show_hint(hint):

        print()

        print(
            Colors.YELLOW
            + "Hint: "
            + hint
            + Colors.RESET
        )

        pause()

    # ------------------------------------------------

    @staticmethod
    def message(text):

        print()

        print(text)

        pause()

    # ------------------------------------------------

    @staticmethod
    def game_over(game):

        clear_screen()

        TerminalUI.banner()

        print(game.display_word)

        print()

        if game.won:

            print(
                Colors.GREEN
                + "YOU WON!"
                + Colors.RESET
            )

        else:

            print(
                Colors.RED
                + "YOU LOST!"
                + Colors.RESET
            )

            print(
                f"The word was: {game.word.value}"
            )

        print()

        print(f"Score: {game.current_score}")

        pause()

    # ------------------------------------------------

    @staticmethod
    def leaderboard(entries):

        clear_screen()

        TerminalUI.banner()

        print("Leaderboard\n")

        if not entries:

            print("No scores recorded.")

        else:

            for i, entry in enumerate(entries, start=1):

                print(
                    f"{i:2}. "
                    f"{entry['name']:<15}"
                    f"{entry['score']:>6}"
                )

        pause()

    # ------------------------------------------------

    @staticmethod
    def statistics(stats):

        clear_screen()

        TerminalUI.banner()

        print("Global Statistics\n")

        for key, value in stats.items():

            print(f"{key:20}: {value}")

        pause()