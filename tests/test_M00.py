"""
Test the tutotiral exercise.
"""

import sys

# add parent directory to path
sys.path.append('..')

import M00Tutorial01 as e1

def test_00_01():
    assert e1.hello_world() == "Hello, World!" 

    
