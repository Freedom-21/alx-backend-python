#!/usr/bin/env python3
"""
This module contains a function that
returns the first element of a sequence
safely using duck-typed annotations.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence if it exists,
    otherwise None.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence or
        None if empty.
    """
    if lst:
        return lst[0]
    else:
        return None
