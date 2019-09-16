"""
Contains tests for app.models.User class
"""
# pylint: disable=redefined-outer-name
from unittest import mock
import pytest
from app.models import Party, Guest

@pytest.fixture
def party1():
    """
    Party object
    """
    return Party(
        email='john@example.com',
    )

@pytest.fixture
def guest1(party1):
    """
    Guest object
    """
    return Guest(
        name='Andreas Arnesson',
        coming=True,
        food="Meat",
        drink="Alcohol",
        party=party1,
    )

@mock.patch("app.models.current_app")
def test_create_invite(_mock_current_app, guest1, party1):
    assert party1.to_dict() == ""
    # assert guest1.party_id == 0

def test_new_user(party1):
    """
    Test that user object contain correct values
    """
    assert party1.email == 'john@example.com'
    assert str(party1) == "<Party None, john@example.com>"

@mock.patch("app.models.current_app")
def test_password_hashing(_mock_current_app, party1):
    """
    Test setting password for user
    """
    party1.set_password('cat')
    assert party1.check_password('dog') is False
    assert party1.check_password('cat') is True

