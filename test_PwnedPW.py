#!/usr/bin/env python3

from PwnedPW import check

def test_answer():
    password = "hello"
    result = check(password)
    assert result[0] == True  # Password was found
    assert result[1] == "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"  # Hash is correct
