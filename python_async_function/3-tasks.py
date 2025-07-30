#!/usr/bin/env python3
"""Create and return an asyncio.Task for wait_random coroutine."""

import asyncio
from 0_basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task object from wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))

