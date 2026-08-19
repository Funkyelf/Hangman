"""
General helper functions.
"""


import json
from pathlib import Path


def clear_screen():
    """
    Clears terminal screen.
    """

    print("\033c", end="")


def load_json(path: Path, default):
    """
    Loads JSON data safely.
    """

    if not path.exists():
        return default

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, IOError):
        return default



def save_json(path: Path, data):
    """
    Saves data as JSON.
    """

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)



def colored(text, color):
    """
    Adds terminal color.
    """

    return f"{color}{text}\033[0m"



def ask_choice(prompt, choices):

    while True:

        answer = input(prompt).lower().strip()

        if answer in choices:
            return answer

        print(f"Choose one of: {', '.join(choices)}")



def pause():

    input("\nPress ENTER to continue...")