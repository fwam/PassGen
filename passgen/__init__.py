#!/usr/bin/env python3
import re
import math
from string import ascii_letters, digits
import secrets

class Entropy:
    def __init__(self, password: str = '') -> None:
        self.password = password

    def _calculate_possible_symbols(self, password: str) -> int:
        possible_symbols = 52  # ascii_letters
        if re.search(r'[0-9]', password):
            possible_symbols += 10  # digits
        if re.search(r'[!@#$%^&*]', password):
            possible_symbols += 8  # symbols
        if re.search(r'[-]', password):
            possible_symbols += 1  # hyphen
        return possible_symbols

    def calculate(self) -> float:
        possible_symbols = self._calculate_possible_symbols(self.password)
        password_length = len(self.password)
        possible_combinations = possible_symbols ** password_length
        return round(math.log2(possible_combinations), 2)

    def to_strength(self, entropy: float) -> str:
        if entropy >= 120:
            return "Very Strong"
        elif entropy >= 60:
            return "Strong"
        elif entropy >= 36:
            return "Weak"
        return "Very Weak"

class Password:
    def __init__(self, length: int = 32, alphanumeric: bool = False, minimum_numbers: int = 0, minimum_symbols: int = 0) -> None:
        self.length = length
        self.alphanumeric = alphanumeric
        self.minimum_numbers = minimum_numbers
        self.minimum_symbols = minimum_symbols

    def validate_query(self) -> None:
        if self.minimum_numbers > self.length:
            raise ValueError("Minimum numbers cannot exceed the length of the password.")
        if self.minimum_symbols > self.length:
            raise ValueError("Minimum symbols cannot exceed the length of the password.")
        if self.minimum_symbols + self.minimum_numbers > self.length:
            raise ValueError("Sum of minimum numbers and symbols cannot exceed the length of the password.")
        if self.alphanumeric and self.minimum_symbols > 0:
            raise ValueError("Minimum symbols must be zero when alphanumeric is True.")

    def generate(self) -> str:
        alphabet = ascii_letters + digits
        if not self.alphanumeric:
            alphabet += "!@#$%^&*"

        self.validate_query()

        while True:
            password = ''.join(secrets.choice(alphabet) for _ in range(self.length))
            if (len(re.findall(r'[!@#$%^&*]', password)) >= self.minimum_symbols and
                len(re.findall(r'[0-9]', password)) >= self.minimum_numbers):
                return password

    def generate_xkcd(self, wordlist: str = '/usr/share/dict/usa') -> str:
        if self.length == 32:
            self.length = 4
        if self.length > 10:
            raise ValueError("XKCD-style password cannot have a length greater than 10.")

        with open(wordlist, 'r') as file:
            words = [x.strip() for x in file if "'" not in x]
        return '-'.join(secrets.choice(words) for _ in range(self.length))
