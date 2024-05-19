#!/usr/bin/env python3
import sys
import re
import argparse
import secrets
import string
import math

def entropy_to_strength(entropy: float) -> str:
    if entropy >= 120:
        return "Very Strong"
    elif entropy >= 60:
        return "Strong"
    elif entropy >= 36:
        return "Weak"
    return "Very Weak"

def _calculate_possible_symbols(password: str) -> int:
    possible_symbols = 52
    if re.search(r'[0-9]', password):
        possible_symbols += 10
    if re.search(r'[!@#$%^&*]', password):
        possible_symbols += 8
    if re.search('[-]', password):
        possible_symbols += 1
    return possible_symbols

def calculate_entropy(password: str) -> float:
    possible_symbols = _calculate_possible_symbols(password)
    password_length = len(password)
    possible_combinations = possible_symbols ** password_length

    return round(math.log2(possible_combinations), 2)

def generate_xkcd_password(length: int) -> str:
    if length > 10:
        raise ValueError("Value of length cannot be greater than 10")
    try:
        with open('/usr/share/dict/usa', 'r') as file:
            words = [x.strip() for x in file if "'" not in x]
    except FileNotFoundError:
        raise FileNotFoundError("The word list file '/usr/share/dict/usa' was not found. Please install the words package.")

    if length <= 0:
        raise ValueError("Value of length must be greater than 0")
    return ''.join(secrets.choice(words) + '-' for _ in range(length)).rstrip('-')

def generate_password(length: int, alpha: bool) -> str:
    alphabet = string.ascii_letters + string.digits
    if not alpha:
        alphabet += "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def __main():
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Generates a password.")
    parser.add_argument('-l', '--length', type=int, default=32, help='Length of the password to generate')
    parser.add_argument('-a', '--alphanumeric', action='store_true', help='Generate an alphanumeric password')
    parser.add_argument('-x', '--xkcd', action='store_true', help='Generate an XKCD-style password')
    args = parser.parse_args()

    if args.length <= 0:
        raise ValueError("Value of length must be greater than 0")

    if args.xkcd and args.alphanumeric:
        raise ValueError("xkcd and alphanumeric cannot be True at the same time.")

    if args.xkcd:
        if args.length == 32:
            length = 4
        password = generate_xkcd_password(args.length)
    else:
        password = generate_password(args.length, args.alphanumeric)

    entropy = calculate_entropy(password)
    print(f'The generated password is: {password}')
    print(f'The calculated entropy of the password is: {entropy}, which makes your password {entropy_to_strength(entropy)}')

if __name__ == "__main__":
    __main()
