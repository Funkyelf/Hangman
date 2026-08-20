"""
Global constants for the Hangman game.
"""

from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"


WORDS_FILE = DATA_DIR / "words.txt"
SCORE_FILE = DATA_DIR / "scores.json"
STATS_FILE = DATA_DIR / "stats.json"
ACHIEVEMENTS_FILE = DATA_DIR / "achievements.json"
SAVE_FILE = DATA_DIR / "savegame.json"


# Difficulty configuration
DIFFICULTIES = {
    "easy": {
        "name": "Easy",
        "min_length": 1,
        "max_length": 4,
        "lives": 7,
        "multiplier": 1
    },

    "medium": {
        "name": "Medium",
        "min_length": 5,
        "max_length": 8,
        "lives": 6,
        "multiplier": 2
    },

    "hard": {
        "name": "Hard",
        "min_length": 9,
        "max_length": 30,
        "lives": 5,
        "multiplier": 3
    }
}


# Scoring
POINTS_CORRECT_LETTER = 10
POINTS_WRONG_LETTER = -5
POINTS_HINT = -20
POINTS_WORD_BONUS = 50
POINTS_WIN = 100
POINTS_LOSS = -50


# Achievements

ACHIEVEMENTS = {
    "first_win": {
        "name": "First Victory",
        "description": "Win your first game"
    },

    "perfect_game": {
        "name": "Perfect Game",
        "description": "Win without mistakes"
    },

    "word_master": {
        "name": "Word Master",
        "description": "Guess 50 words"
    },

    "hard_mode": {
        "name": "Challenge Accepted",
        "description": "Win a hard difficulty game"
    },

    "no_hints": {
        "name": "Pure Skill",
        "description": "Win without using hints"
    }
}


# Terminal colors

class Colors:
    RESET = "\033[0m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"

    BOLD = "\033[1m"


# Hangman drawings

HANGMAN = [

"""
 +---+
     |
     |
     |
    ===
""",

"""
 +---+
 O   |
     |
     |
    ===
""",

"""
 +---+
 O   |
 |   |
     |
    ===
""",

"""
 +---+
 O   |
/|   |
     |
    ===
""",

"""
 +---+
 O   |
/|\\  |
     |
    ===
""",

"""
 +---+
 O   |
/|\\  |
/    |
    ===
""",

"""
 +---+
 O   |
/|\\  |
/ \\  |
    ===
"""
]