#!/usr/bin/env python3
"""
This module contains a function that
safely gets a value from a dictionary using type annotations.
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to get the value from.
        key (Any): The key whose value is to be retrieved.
        default (Union[T, None]): The default value to
        return if key is not found.

    Returns:
        Union[Any, T]: The value corresponding to
        the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
