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
# Fixtures
# --------------------------------------------------------------------------------

# if you use yield is a generator.
@pytest.fixture
def accu():
    return Accumulator()


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_accumulator_init(accu):
    assert accu.count == 0


def test_accumulator_add_one(accu):
    accu.add()
    assert accu.count == 1


def test_accumulator_add_three(accu):
    accu.add(3)
    assert accu.count == 3


def test_accumulator_add_twice(accu):
    accu.add()
    accu.add()
    assert accu.count == 2


def test_accumulator_cannot_set_count_directly(accu):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accu.count = 10
