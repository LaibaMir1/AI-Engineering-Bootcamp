import pytest
from age import is_adult


def test_age_17_is_not_adult():
    assert is_adult(17) is False


def test_age_18_is_adult():
    assert is_adult(18) is True


def test_negative_age_raises_error():
    with pytest.raises(ValueError):
        is_adult(-1)