#!/usr/bin/env python3
"""Measure average runtime of wait_n coroutine."""

import time
import asyncio
from concurrent_coroutines import wait_n  # adapte ce nom selon ton renommage


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return the average time per coroutine (total_time / n).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n

