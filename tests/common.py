import random


def rand_min_max(min, max, need_round=False):
    val = min + random.random() * (max - min)
    if need_round:
        val = round(val)

    return val
