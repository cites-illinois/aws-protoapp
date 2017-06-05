from __future__ import print_function

import os
import sys
import unittest

os.environ['DJANGO_SETTINGS_MODULE'] = 'protoapp.settings'

import django
from django.conf import settings
from django.test.utils import get_runner

#####

def get_test_suite(test_dir):
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(test_dir, pattern='test_*.py')
    return test_suite

#####

def run_tests(test_suite):
    print(get_runner(settings))
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    sys.exit(9)

    failures = test_runner([], verbosity=1, interactive=True)
    sys.exit(failures)

#####

if __name__ == '__main__':
    test_dir = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, test_dir)

    django.setup()

    test_suite = get_test_suite(test_dir)
    run_tests(test_suite)
