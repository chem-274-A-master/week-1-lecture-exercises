"""
Test the Errors and Exceptions module.
"""

import os
import sys

import pytest

# get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# add the parent directory to the path
sys.path.append(parent_dir)

def test_01_01():
    import M01ErrorsExceptions01 as e1
    
def test_01_02():
    import M01ErrorsExceptions02 as e2

    with pytest.raises(IndexError):
        e2.call_element()
    

def test_01_03():
    import M01ErrorsExceptions03 as e3

    my_list = [1, 49, 9, 46, 4, 33, 9, "the last element"]

    assert e3.safe_list(my_list, 1) == 49
    assert e3.safe_list(my_list, 100) == "the last element"


def test_01_04_case1():
    import M01ErrorsExceptions04 as e4

    weights = [0.1, 0.5, 0.4, 0.9]

    vals = [ 5, 10, 1 ]

    with pytest.raises(ValueError):
        e4.weighted_average(vals, weights)

def test_01_04_case2():
    import M01ErrorsExceptions04 as e4

    weights = [0.1, 0.5, 0.4]
 
    vals = [ 5, 10, 1 ]

    assert e4.weighted_average(vals, weights) == 5.9
