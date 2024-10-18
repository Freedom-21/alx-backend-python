#!/usr/bin/env python3
"""
This module contains a function that
sums a list of floats with type annotations.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats.
    """
    return sum(input_list)
