"""
Bot Configuration class definition

Configuration setups for the following:
    Database
"""

import logging
import os

from src.database.sql.database import Database


class Configuration:  # pylint: disable=R0903
    """
    Defines the configuration of the program
    It is used to configure the program with various APIs
    for preprocessing and analysis
    """

    def __init__(self, ctx: dict) -> None:
        """
        Sets up a context dictionary containing the configuration details
        """
        self.ctx = ctx

    def setup_database(self) -> str:
        """Sets up the database"""

        if os.path.exists(os.path.join(os.getcwd(), "data", f"{self.ctx}.db")):
            logging.info("Database already exists")
            database = Database("")
            self.ctx["database"] = database  # type: ignore
            return ">>> Database setup successfully!"

        # Creation
        res = input(">>> Database not found...Set up now? (y/n)\n>")
        if res.lower() == "y":
            self._create_databases()
        return ">>> Database created successfully!"

    def _create_databases(self):
        """Creates and sets up database"""

        # Set up blank databases
        users_db = Database("users")
        translator_db = Database("translator")
        self.ctx["user_database"] = users_db
        self.ctx["translator_database"] = translator_db

        # Set up users tables

        # Set up translator tables
        translator_db.create_table("users", "id TEXT")  # users
        # translator_db.create_table( # user_favorites
        #     "user_favorites",
        #     "FOREIGN KEY (sentence_id) REFERENCES sentences(sentence_id), "
        #     "FOREIGN KEY (meaning_id) REFERENCES meaning(meaning_id), "
        #     "FOREIGN KEY (favorited_at) REFERENCES sentences(favorited_at), "
        #     "PRIMARY KEY (favorites_id)"
        # )
        translator_db.create_table(  # sentences
            "sentences",
            "sentence_id TEXT, "
            "sentence TEXT, "
            "favorited_at TIMESTAMP, "
            "PRIMARY KEY (sentence_id)",
        )
        translator_db.create_table(  # meaning
            "meaning",
            "meaning_id TEXT, "
            "sentence_id TEXT, "
            "meaning TEXT, "
            "PRIMARY KEY (meaning_id), "
            "FOREIGN KEY (sentence_id) REFERENCES sentences(sentence_id)",
        )
