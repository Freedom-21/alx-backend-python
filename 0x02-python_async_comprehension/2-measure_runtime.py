#!/usr/bin/env python3
"""
This module defines a coroutine that measures the
runtime of parallel async comprehensions.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension
    our times in parallel and measures total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
                        async_comprehension(),
                        async_comprehension(),
                        async_comprehension(),
                        async_comprehension()
                        )
    total_time = time.time() - start_time
    return total_time
