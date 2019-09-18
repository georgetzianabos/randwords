import random


def generate(words, count):

    results = []

    while len(results) <= count:

        new_words = words.copy()

        random.shuffle(new_words)

        results += new_words

    return results[:count]
