#!/usr/bin/env python3
"""
This module contains a function that sums a
list of integers and floats with type annotations.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the elements.
    """
    return sum(mxd_lst)
