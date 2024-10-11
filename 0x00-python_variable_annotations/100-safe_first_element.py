#!/usr/bin/env python3
"""Task 100 Advanced"""
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence or None if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
