"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
from ..stuff.accum import Accumulator


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_accumulator_init():
    accu = Accumulator()
    assert accu.count == 0


def test_accumulator_add_one():
    accu = Accumulator()
    accu.add()
    assert accu.count == 1


def test_accumulator_add_three():
    accu = Accumulator()
    accu.add(3)
    assert accu.count == 3


def test_accumulator_add_twice():
    accu = Accumulator()
    accu.add()
    accu.add()
    assert accu.count == 2


def test_accumulator_cannot_set_count_directly():
    accu = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accu.count = 10

