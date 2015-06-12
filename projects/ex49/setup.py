try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Artur Tsuda',
    'url': '',
    'download_url': '',
    'author_email': 'artur.o.tsuda@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
