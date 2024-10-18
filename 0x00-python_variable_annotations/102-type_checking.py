#!/usr/bin/env python3
"""
This module contains a function that
zooms in on an array with type checking.
"""
from typing import Tuple, List


def zoom_array(
    lst: Tuple,
    factor: int = 2
) -> List:
    """
    Zoom into an array by repeating each element
    a specified number of times.

    Args:
        lst (Tuple): A tuple to zoom into.
        factor (int): The factor by which to
        repeat each element (default is 2).

    Returns:
        List: A list with each element repeated by the given factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
