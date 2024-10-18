#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of asynchronous coroutines.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of `wait_n(n, max_delay)` and return the average time per coroutine.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        float: The average runtime per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
