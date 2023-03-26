from sentences import get_determiner, get_noun, get_verb, \
get_preposition, get_prepositional_phrase, make_sentence
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(11):
        word = get_noun(1)
    
    assert word in single_nouns

    # 2. Test the plural nouns.
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(11):
        word = get_noun(2)
    
    assert word in plural_nouns


def test_get_verb():
    # 1. Test the past verbs.
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]
    
    # Single sentences
    for _ in range(11):
        word = get_verb(1,"past")
    assert word in past_verbs

    # Plural sentences
    for _ in range(11):
        word = get_verb(2, "past")
    assert word in past_verbs

    # 2. Test the present verbs.
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]

    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]

    # Single present verbs.   
    for _ in range (11):
        word = get_verb(1, "present")
    assert word in single_present_verbs

    # Plural present verbs.
    for _ in range (11):
        word = get_verb(2, "present")
    assert word in plural_present_verbs

    # 3. Test the future verbs.
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]
    
    # Single sentences
    for _ in range (11):
        word = get_verb(1, "future")
    assert word in future_verbs

    # Plural sentences
    for _ in range (11):
        word = get_verb(2, "future")
    assert word in future_verbs

def test_get_preposition():
    # calls get_preposition and uses assert to verify that the value 
    # returned from get_preposition is correct.

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    
    for _ in range(31):
        word = get_preposition()
    assert word in prepositions


def test_get_prepositional_phrase():
    #  calls get_prepositional_phrase and uses assert to verify that
    # the value returned from get_prepositional_phrase is correct.

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["some", "many", "the"]

    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]

    # Test Single Prepositional Phrases
    single_prepositional_phrase = get_prepositional_phrase(1).split(" ")
    if len(single_prepositional_phrase) == 3:
        assert single_prepositional_phrase[0] in prepositions
        assert single_prepositional_phrase[1] in single_determiners
        assert single_prepositional_phrase[2] in single_nouns
    
    # Test Plural Prepositional Phrases
    plural_prepositional_phrase = get_prepositional_phrase(2).split(" ")
    if len(plural_prepositional_phrase) == 3:
        assert plural_prepositional_phrase[0] in prepositions
        assert plural_prepositional_phrase[1] in plural_determiners
        assert plural_prepositional_phrase[2] in plural_nouns


def test_make_sentence():
    test_get_determiner()
    test_get_noun()
    test_get_verb()
    test_get_preposition()
    test_get_prepositional_phrase()


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
