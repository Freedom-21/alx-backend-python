#!/usr/bin/env python3
"""
This module contains a function that returns
a tuple with a string and the square of a number with type annotations.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with a string and the square of an int/float.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of v.
    """
    return (k, float(v ** 2))
