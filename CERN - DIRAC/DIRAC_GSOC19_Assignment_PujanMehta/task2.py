""" Simple test on using mock
"""

import mock
import pytest


#########################
# function to test


def myFunction(objectIn):
    """ what you are supposed to test
    """
    return objectIn.aMethodToMock() + 2


#########################
# Actual test


@pytest.fixture
def objectMock():
    """ A fixture to create a fake object as we want it"""
    fakeObject = mock.MagicMock()
    # Newly added line.
    fakeObject.aMethodToMock.return_value = 3

    return fakeObject

def test_myFunction(objectMock):
    """ Test myFunction """
    assert myFunction(objectMock) == 5


