#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
