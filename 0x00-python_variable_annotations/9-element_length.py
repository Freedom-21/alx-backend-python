#!/usr/bin/env python3
"""
This module contains a function that
returns a list of tuples containing each
element and its length with type annotations.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]:
        A list of tuples containing each element and its length.
    """
    return [(i, len(i)) for i in lst]
