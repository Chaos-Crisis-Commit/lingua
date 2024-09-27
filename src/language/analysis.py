# type: ignore
"""Module for sentence analysis when breaking down sentences and their meanings"""

from PyMultiDictionary import MultiDictionary
import nltk
from nltk.corpus import wordnet

dictionary = MultiDictionary()


def get_full_analysis_of(text):
    """Breaks down text into smaller parts"""

    res = {}

    # Split the sentence into words
    words = text.split()

    # Get meanings
    for word in words:
        final_word_breakdown = {}

        # Check word's lemmas (if contraction, etc)
        # TODO

        # Get meaning, associations, and POS tags
        meaning = get_meaning("en", word)
        # Clean output
        # TODO

        associations = get_associations(word)
        # Clean output
        # TODO

        pos = tag(word)
        # Clean output
        # TODO

        # Add
        final_word_breakdown["meaning"] = meaning
        final_word_breakdown["associations"] = associations

        # Add word to final dict
        res[word] = final_word_breakdown

    # Breakdown POS for whole sentence
    final_word_breakdown["part_of_speech"] = pos

    return res


def get_meaning(translation_language, text):
    """Gets meaning of word"""

    return dictionary.meaning(translation_language, text)


def get_associations(text):
    """Get association of words like synonyms and antonyms"""
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(text):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    # Tag and add to dict
    return (synonyms, antonyms)


def tag(text):
    """Returns part of speech as tag for current word"""
    tag = nltk.pos_tag([text])

    # Use POS enum to associate tag with word
    return tag


if __name__ == "__main__":
    TEXT_INPUT = "It's a good day today!"
    analysis = get_full_analysis_of(TEXT_INPUT)
    print(f"length: {len(analysis)}")
    print(analysis)
