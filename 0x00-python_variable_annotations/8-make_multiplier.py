#!/usr/bin/env python3
"""Task number 8"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
