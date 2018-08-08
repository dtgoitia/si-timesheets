import pytest
from sit.cli import validate_day_status


@pytest.mark.parametrize('value, raises_exception', (
    (-99, True),
    (-1, True),
    (0, False),
    (1, False),
    (2, False),
    (3, False),
    (4, False),
    (5, False),
    (6, False),
    (7, True),
    (99, True),
    ('a', True),
    ('abcd', True),
    ([0, 1], True),
    ({'a': 1}, True),
))
def test_validate_day_status(value: int, raises_exception: bool):
    if raises_exception:
        with pytest.raises(Exception):
            validate_day_status(value)
    else:
        expected_result = value
        actual_result = validate_day_status(value)
        assert expected_result == actual_result
