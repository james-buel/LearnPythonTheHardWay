try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 47 from LearnPythonTheHardWay',
    'author': 'Artur Tsuda',
    'url': '',
    'download_url': '',
    'author_email': 'artur.o.tsuda@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
