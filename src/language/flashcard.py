"""
Module used for flashcard creation
"""

import src.language.analysis as analysis


class Flashcard:
    def __init__(self, origin_language, target_language, sentence, translation) -> None:
        # self.database = Database(target_language)
        self.sentence = sentence

    def create_flashcard(self):
        """Takes breakdowns of sentence and creates a flashcard entry"""
        # Create initial flashcard with straight meaning and translation

        # Break down sentence
        breakdown_individual = analysis.breakdown(self.sentence)

        # Add words to database

        # Grab breakdown for structure
        breakdown_syntax = None

        # Add structure to database?

        # Grab breakdown for words
