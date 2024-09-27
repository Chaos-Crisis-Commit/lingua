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
from database.sql.database import Database

ctx = {"database": ""}


def help_lingua(command_help):
    """Return help on command"""
    command_help = command_help[0]
    if not command_help:
        print(
            "Lingua bot is a language learning bot meant to aid and assist in"
            "\nthe creation of flashcards, generative sentences, and overall"
            "\npersonalized learning experience for the user."
            "\nThis project is one of the first steps to test basic functionality"
            "\nof the future bot, through an interface that is easier"
            "\nto access than running the bot itself.\n\n"
            "Through this CLI the following commands can be run:"
            "\n\tadduser"
            "\n\taddsentence"
            "\n\ttestquiz\n"
            "Enter a command to learn more"
        )
        command_help = input(">>> ")
        print("")

    if command_help == "adduser":
        print("\nadduser")
        print("Simulates adding new user to the database based on given information\n")
    if command_help == "addsentence":
        print("\naddsentence")
        print(
            "Simulates adding a sentence by breaking down word by word and adding to a DB"
        )
    if command_help == "testquiz":
        print("\ntestquiz")
        print("Simulates creating a quiz with entries in the DB")
    print("")


def add_user(info):
    print("adduser")
    print(f"Adding user with info: {info}")


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

    command_args = text.split()
    commands[command_args[0]](command_args[1:])


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
    ctx["database"] = Database("users_test")
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
