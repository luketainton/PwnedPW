#!/usr/bin/env python3

"""Test cases for app/main.py."""

from typing import Union

from app.main import check, hash_password

PASSWORD = "hello"
EXPECTED_HASH = "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"


def test_hash_password() -> None:
    """Test case for hash_password()."""
    result: Union[tuple, bool] = hash_password(PASSWORD)
    assert result == (EXPECTED_HASH[:5], EXPECTED_HASH[5:])


def test_check_common_password() -> None:
    """Test case for check() with common password."""
    result: Union[tuple, bool] = check(PASSWORD)
    assert result[0] is True  # Password was found
    assert result[1] == EXPECTED_HASH  # Hash is correct


def test_check_uncommon_password() -> None:
    """Test case for check() with uncommon password."""
    result: Union[tuple, bool] = check("tjzdp6eguZ9q4puPAiXWc6NM")
    assert result is False  # Password was not found
