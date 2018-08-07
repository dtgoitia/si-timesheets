import datetime
import pytest
from sit.friday import get_previous_friday


@pytest.fixture
def expected_prior_week():
    return datetime.datetime(2018, 3, 16)


@pytest.fixture
def expected_this_week():
    return datetime.datetime(2018, 3, 23)


def test_monday(expected_prior_week):
    assert expected_prior_week, get_previous_friday(datetime.datetime(2018, 3, 19))


def test_tuesday(expected_prior_week):
    assert expected_prior_week, get_previous_friday(datetime.datetime(2018, 3, 20))
  

def test_wednesday(expected_prior_week):
    assert expected_prior_week, get_previous_friday(datetime.datetime(2018, 3, 21))
  

def test_thursday(expected_prior_week):
    assert expected_prior_week, get_previous_friday(datetime.datetime(2018, 3, 22))
  

def test_friday(expected_this_week):
    assert expected_this_week, get_previous_friday(datetime.datetime(2018, 3, 23))
  

def test_saturday(expected_this_week):
    assert expected_this_week, get_previous_friday(datetime.datetime(2018, 3, 24))
  
  
def test_sunday(expected_this_week):
    assert expected_this_week, get_previous_friday(datetime.datetime(2018, 3, 25))