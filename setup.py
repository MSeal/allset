import os
from setuptools import setup

def read(fname):
    # Utility function to read the README file.
    with open(os.path.join(os.path.dirname(__file__), fname)) as fhandle:
        return fhandle.read()

setup(
    name='allset',
    version="1.0.0",
    description='Generates dynamic bindings for module imports',
    long_description=read('README.md'),
    packages=['allset'],
    author='Matthew Seal',
    author_email='mseal@opengov.com',
    url='https://github.com/OpenGov/allset',
    download_url='https://github.com/OpenGov/allset/tarball/v1.0.0',
    keywords=['importing'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2 :: Only'
    ]
)
