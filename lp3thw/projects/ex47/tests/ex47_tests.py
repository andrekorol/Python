from nose.tools import *
import ex47
import os.path
from subprocess import call
from math import *

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')
