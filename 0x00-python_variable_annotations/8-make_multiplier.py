#!/usr/bin/env python3
"""
This module contains a function that
returns a multiplier function with type annotations.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]:
        A function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
