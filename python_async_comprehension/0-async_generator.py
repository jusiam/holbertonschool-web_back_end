#!/usr/bin/env python3
"""Write a coroutine called async_generator"""


import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """result"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
