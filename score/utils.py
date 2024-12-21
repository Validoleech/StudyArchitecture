import random

def generate_score(good=False):
    """Создание случайного score."""
    if good:
        return random.uniform(0.5, 1.0)
    return random.uniform(0.0, 1.0)