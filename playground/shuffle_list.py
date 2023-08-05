import random


def shuffle_list(target: list) -> list:
    shuffled_list = []
    for i in target:
        shuffled_list.append(i)
    random.shuffle(shuffled_list)
    return shuffled_list
