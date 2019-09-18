"""Randomise word list

Usage:
  randwords <words>... [--count=<number>]

--count=number  The number of words to generate [default: 100]

"""
import sys

from docopt import docopt

from randwords import generate


def cli():

    arguments = docopt(__doc__)

    results = generate(
        words=arguments['<words>'],
        count=int(arguments['--count']),
    )

    sys.stdout.write(' '.join(results) + '\n')