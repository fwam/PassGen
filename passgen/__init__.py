#!/usr/bin/env python3
import re
import math
from string import ascii_letters, digits
import secrets

class Entropy:
    def __init__(self, password=''):
        self.password = password
        pass
    def _calculate_possible_symbols(self, password: str) -> int:
        possible_symbols: int = 52
        if re.search(r'[0-9]', password):
            possible_symbols += 10
        if re.search(r'[!@#$%^&*]', password):
            possible_symbols += 8
        if re.search('[-]', password):
            possible_symbols += 1
        return possible_symbols

    def calculate(self) -> float:
        possible_symbols: int = self._calculate_possible_symbols(self.password)
        password_length: int = len(self.password)
        possible_combinations = possible_symbols ** password_length
        # Return entropy rounded to two digits after comma.
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
    def __init__(self, length: int, alphanumeric: bool = False, minimum_numbers: int = 0, minimum_symbols: int = 0) -> None:
        self.length = length
        self.alphanumeric = alphanumeric
        self.minimum_numbers = minimum_numbers
        self.minimum_symbols = minimum_symbols

    def validate_query(self):
        if (self.minimum_numbers > self.length):
            raise ValueError("Minimums cannot exceed length of the password.")
        if (self.minimum_symbols > self.length):
            raise ValueError("Minimums cannot exceed length of the password.")
        if (self.minimum_symbols+self.minimum_numbers > self.length):
            raise ValueError("Minimums cannot exceed length of the password.")
        if (self.alphanumeric and self.minimum_symbols>0):
            raise ValueError("minimum_symbols must be zero, when alphanumeric is True")

    def generate(self) -> str:
        alphabet = ascii_letters + digits
        if not self.alphanumeric:
            alphabet += "!@#$%^&*"
        if self.length == None:
            self.length = 32
        self.validate_query()

        password = ''.join(secrets.choice(alphabet) for _ in range(self.length))
        while ((len(re.findall('[!@#$%^&*]', password)) < self.minimum_symbols) or (len(re.findall('[0-9]', password)) < self.minimum_numbers)):
                password = ''.join(secrets.choice(alphabet) for _ in range(self.length))
        return password

    def generate_xkcd(self, wordlist = '/usr/share/dict/usa'):
        if self.length == None:
            self.length = 4
        if self.length > 10:
            raise ValueError("XKCD-style password cannot have the length greater than 10.")
        with open(wordlist, 'r') as file:
            words = [x.strip() for x in file if "'" not in x]
        return '-'.join(secrets.choice(words) for _ in range(self.length))
