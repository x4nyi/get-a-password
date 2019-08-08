import random
import string

from .conf import DEFAULT_LENGTH

def generate(length = DEFAULT_LENGTH):
    print(''.join(random.choice(string.punctuation + string.digits + string.ascii_uppercase + string.ascii_lowercase) for _ in range(length)))
