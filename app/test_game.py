import pytest

def test_invalid_input_crash():
    with pytest.raises(ValueError):
        int("123") 