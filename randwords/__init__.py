import random

from .__version__ import __title__, __version__, __description__, __author__


def generate(words, count):

    results = []

    while len(results) <= count:

        new_words = words.copy()

        random.shuffle(new_words)

        results += new_words

    return results[:count]
