import secrets
from string import digits, ascii_letters


ALPHABET = digits + ascii_letters


def make_random_string(length, alphabet=ALPHABET):
    return ''.join(secrets.choice(alphabet) for _ in range(length))
