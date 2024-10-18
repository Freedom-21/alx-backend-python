#!/usr/bin/env python3
"""
This module contains an asynchronous function that runs multiple coroutines concurrently.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `wait_random` n times concurrently and return the list of delays in ascending order.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

