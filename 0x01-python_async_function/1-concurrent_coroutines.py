#!/usr/bin/env python3
""" Task number two """
import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    
    result = []
    while delays:
        min_delay = min(delays)
        result.append(min_delay)
        delays.remove(min 
