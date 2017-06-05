from __future__ import print_function

import os
import unittest

from datetime import datetime
from setuptools import find_packages, setup

from protoapp import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

#####

def get_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('test', pattern='test_*.py')
    return test_suite

#####

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='protoapp',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'bcrypt',
        'Django>=1.9,<1.10',
        'djangorestframework',
    ],
#   license='BSD License',  # example license
    description='A simple Django app to test automated deployment.',
    long_description=README,
    test_suite='setup.get_test_suite',
    url='https://www.illinois.edu/',
    author='Jon R. Roma',
    author_email='roma@illinois.edu',
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Programming Language :: Python :: 2.7',
        'University of Illinois at Urbana-Champaign',
        'Technology Services',
    ],
)
