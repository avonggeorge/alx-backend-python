#!/usr/bin/env python3
'''
Get a random float between 0 and max_delay,
Asynchronously wait for the delay
Return the actual delay
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
