import random


def get_word() -> str:
    words = [
        "limonade",
        "elephant",
        "computer",
        "python",
        "microsoft",
        "table",
        "world",
        "kitchen",
        "television",
        "carpet",
        "bathroom",
        "balcony",
        "house",
        "network",
        "garage",
        "logistic",
        "country",
        "vilage",
        "wallpaper",
        "docker",
    ]
    return random.choice(words)
