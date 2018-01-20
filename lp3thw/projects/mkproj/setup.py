try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':
    'Creates a new project based on the deafult project skeleton',
    'author': 'Andre Rossi Korol',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'anrobits@yahoo.com.br',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mkproj'],
    'scripts': ['bin/mkproj.py'],
    'name': 'mkproj'
}

setup(**config)
