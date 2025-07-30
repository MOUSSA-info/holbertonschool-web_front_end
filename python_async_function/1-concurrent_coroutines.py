#!/usr/bin/env python3

import asyncio
import importlib

mod = importlib.import_module("0-basic_async_syntax")
wait_random = mod.wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

