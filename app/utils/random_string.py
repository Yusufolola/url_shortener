import string
import random

def generate_random_string(length: int) -> str:
    """
    Generates a random string of a given length consisting of letters and digits.
    """
    strings = string.ascii_letters + string.digits
    return ''.join(random.choice(strings) for _ in range(length))

