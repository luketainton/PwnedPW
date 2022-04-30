#!/usr/bin/env python3

"""Test cases for pwned_pw.py."""

from app.pwned_pw import hash_password, check


PASSWORD = "hello"
EXPECTED_HASH = "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"


def test_hash_password():
    """Test case for hash_password()."""
    result = hash_password(PASSWORD)
    assert result == (EXPECTED_HASH[:5], EXPECTED_HASH[5:])


def test_check():
    """Test case for check()."""
    result = check(PASSWORD)
    assert result[0] is True  # Password was found
    assert result[1] == EXPECTED_HASH  # Hash is correct
