# PassGen - a very simple password generator
TL;DR – I was looking for some simple project to create, learning Python.
I guess here it is.

# Usage
## As a standalone program
`python main.py [-h] [-l LENGTH] [-a] [-x/--xkcd]`

### Options:
  - `-h` - Provides with a help page
  - `-l` - Generates a password with a defined length (default: 32 (or 4 if it's -x))
  - `-a` - Generates an alphanumeric password (default: false)
  - `-x` - Generates a password in XKCD style (default: false)

## As a library.
There are few modules you can use.
- `generate_password(length: int, alpha: bool) -> str` – Returns a standard password.
- `generate_xkcd_password(length: int) -> str` – Returns an  XKCD-style password.
- `calculate_entropy(password: str) -> float` – Returns entropy of a password.
- `entropy_to_strength(entropy: float) -> str` – Returns strength of a password.

## Notes:
- Max XKCD-style password length is 10 words.
- XKCD-style passwords require the `words` package.
- You can't use `-a` and `-x` at the same time.

## To-Do:
- Randomly add numbers to XKCD-style passwords.
- Randomly capitalize words in XKCD-style passwords.
