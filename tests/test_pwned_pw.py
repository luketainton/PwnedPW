#!/usr/bin/env python3

from app.pwned_pw import hash_password, check


password = "hello"
expected_hash = "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"


def test_hash_password():
    result = hash_password(password)
    assert result == (expected_hash[:5], expected_hash[5:])


def test_answer():
    password = "hello"
    result = check(password)
    assert result[0] == True  # Password was found
    assert result[1] == expected_hash  # Hash is correct
