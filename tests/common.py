import random
from typing import Union


def rand_min_max(min: int, max: int, need_round: bool = False) -> Union[int, float]:
    val = min + random.random() * (max - min)
    if need_round:
        val = round(val)

    return val
