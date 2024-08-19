"""
Test the tutotiral exercise.
"""

import os
import sys

# get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# add the parent directory to the path
sys.path.append(parent_dir)

import M00Tutorial01 as e1

def test_00_01():
    assert e1.hello_world() == "Hello, World!" 

    
