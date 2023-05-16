#!/usr/bin/env python3

"""Checks if a password has been leaked."""

import getpass
import hashlib
from typing import Union

import requests


def hash_password(pw_in) -> tuple:
    """Take password as input, hash it in SHA-1, and split it for use later on"""
    pw_hash: hashlib._Hash = hashlib.sha1()
    pw_hash.update(str.encode(pw_in))
    digest: str = pw_hash.hexdigest()
    return (digest[:5], digest[5:])


def get_pwned_hashes(api_param) -> list:
    """Query the API for all hashes matching the input string"""
    returned_hashes: list = []
    res: requests.Response = requests.get(
        f"https://api.pwnedpasswords.com/range/{api_param}", timeout=10, stream=True
    )
    for line in res.iter_lines():
        if line:
            returned_hashes.append(line.decode().split(":"))
    return returned_hashes


def check(password: str) -> Union[tuple, bool]:
    """Run password check"""
    # Get the split hash of the password
    pw_hash_array: tuple = hash_password(password)
    # Send first 5 chars to API to retrieve matching hashes
    possible_hashes: list = get_pwned_hashes(pw_hash_array[0])
    # For each hash, test for a match
    for possible_hash in possible_hashes:
        if pw_hash_array[1].upper() == possible_hash[0]:
            identified_hash: str = pw_hash_array[0] + pw_hash_array[1]
            occurences: int = possible_hash[1]
            return (True, identified_hash, occurences)
    return False


def main() -> None:  # pragma: no cover
    """Main function"""
    # Get password
    password: str = getpass.getpass()
    # Run check
    result: Union[tuple, bool] = check(password)
    if isinstance(result, tuple) and result[0]:
        print(f"Password found as hash {result[1]}")
        print(f"Occurrences: {result[2]}")
    else:
        print("Password not found.")


if __name__ == "__main__":  # pragma: no cover
    main()
