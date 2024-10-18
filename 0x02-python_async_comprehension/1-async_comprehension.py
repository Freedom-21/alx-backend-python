#!/usr/bin/env python3
"""
This module defines a coroutine that uses an async comprehension.
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async
    comprehension over async_generator.

    Returns:
        List[float]: List of 10 random numbers collected.
    """
    return [i async for i in async_generator()]
