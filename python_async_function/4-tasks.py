#!/usr/bin/env python3
"""Run task_wait_random n times with max_delay concurrently and return sorted delays."""

import asyncio
from typing import List
from 3_tasks import task_wait_random  # adapte le nom du module selon ton renommage

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and return the list
    of all delays in ascending order (natural order of completion).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

