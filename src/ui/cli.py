# pylint: disable-all
# type: ignore
"""
Test Utility and main functionality of bot
Gives verbose feedback on processes using debug logger

Current Functionalities:
    User creation
    Quiz Creation
    Flashcard Creation
    Flashcard Recall
"""

import pathlib
import json
import logging
import sys


def help_lingua():
    print("help")


def add_user():
    print("adduser")


def add_sentence():
    print("addsentence")


def test_quiz():
    print("testquiz")


def parse_input(text):
    """Command interaction

    Allows user to manipulate data for testing purposes in the confines of test data/db
    List of commands:
        help
        adduser
        addsentence
        testquiz
    """
    commands = {
        "help": help_lingua,
        "adduser": add_user,
        "addsentence": add_sentence,
        "testquiz": test_quiz,
    }

    commands[text]()


def cli():
    """Run CLI"""

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    print("\n\nLingua Bot test CLI")
    print(
        "Test Utility and main functionality of bot\n\n"
        "\tCurrent Functionalities:\n"
        "\tUser creation\n"
        "\tQuiz Creation\n"
        "\tFlashcard Creation\n"
        "\tFlashcard Recall\n\n"
    )

    # Test config
    # Set up ctx
    ctx = {"database": []}  # type: ignore
    # config = Configuration(ctx)

    # Database
    print("...Instantiating test database...\n")
    # if not ctx["database"]:
    #    config.setup_database()

    # User
    # user_path = input("Path to test user JSON (if applicable)\n>>>")
    user_path = None
    if not user_path:
        user_path = pathlib.Path(pathlib.Path.cwd(), "data\\test\\user_example.json")

    with open(user_path) as f:
        user = json.load(f)

    print("...current user:")
    print(user)

    # Done
    print("\n...Done with instantiation...\n")

    # Get input
    user_in = ""
    while user_in != "quit":
        user_in = input("Input command, for list of commands type 'help':\n>>> ")
        if user_in == "quit":
            continue
        parse_input(user_in)


if __name__ == "__main__":
    cli()
