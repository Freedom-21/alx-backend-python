#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio task from an asynchronous coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task from the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio task created from wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
