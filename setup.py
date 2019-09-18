import os
import setuptools


here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'randwords', '__version__.py')) as handle:
    exec(handle.read(), about)

    
setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt>=0.6.2'
    ],
    entry_points={
        'console_scripts': [
            'randwords = randwords.cli:cli'
        ],
    },
    python_requires='>=3.5'
)