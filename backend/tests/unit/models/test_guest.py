"""
Contains tests for app.models.Guest class
"""
# pylint: disable=redefined-outer-name
import pytest
from app.models import Guest

@pytest.fixture
def guest1():
    """
    Guest object
    """
    return Guest(
        name='Andreas Arnesson',
        coming=True,
        food="Meat",
        drink="Alcohol",
        party_id=0,
    )



def test_new_post(guest1):
    """
    Test that post contain correct value
    """
    assert guest1.name == 'Andreas Arnesson'
    assert guest1.coming is True
    assert guest1.food == "Meat"
    assert guest1.drink == "Alcohol"
    assert guest1.allergy is None
    assert str(guest1) == "<Guest: Andreas Arnesson, coming: True with party 0>"