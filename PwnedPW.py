#!/usr/bin/env python3


import requests
import hashlib
import getpass


def hash_password(pw_in):
    """Take password as input, hash it in SHA-1, and split it for use later on"""
    hash = hashlib.sha1()
    hash.update(str.encode(pw_in))
    digest = hash.hexdigest()
    return [digest[:5], digest[5:]]


def get_pwned_hashes(api_param):
    """Query the API for all hashes matching the input string"""
    returned_hashes = []
    r = requests.get(f"https://api.pwnedpasswords.com/range/{api_param}", stream=True)
    for line in r.iter_lines():
        if line:
            returned_hashes.append(line.decode().split(":"))
    return returned_hashes


def check(password: str) -> tuple:
    # Get the split hash of the password
    pw_hash_array = hash_password(password)
    # Send first 5 chars to API to retrieve matching hashes
    possible_hashes = get_pwned_hashes(pw_hash_array[0])
    # For each hash, test for a match
    for h in possible_hashes:
        if pw_hash_array[1].upper() == h[0]:
            identified_hash = pw_hash_array[0] + pw_hash_array[1]
            occurences = h[1]
            return (True, identified_hash, occurences)
    return (False)


def main():
    """Main function"""
    # Get password
    pw = getpass.getpass()
    # Run check
    result = check(pw)
    if result[0]:
        print(f"Password found as hash {result[1]}")
        print(f"Occurrences: {result[2]}")


if __name__ == "__main__":
    main()
