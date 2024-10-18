#!/usr/bin/env python3
"""
This module contains an asynchronous function that runs multiple tasks concurrently.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `task_wait_random` n times concurrently and return the list of delays in ascending order.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
