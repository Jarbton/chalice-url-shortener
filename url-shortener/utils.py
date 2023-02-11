import random
import string


def get_short_url():
    """Generates a short url using a random string of characters."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(6))


def store_url(short_url, url):
    """Stores the url in the database."""
    pass


def get_long_url(short_url):
    """Retrieves the url from the database."""
    return None
