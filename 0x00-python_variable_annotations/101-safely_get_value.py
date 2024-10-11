#!/usr/bin/env python3
"""Task 101 Advanced"""
from typing import Mapping, Any, Union, TypeVar

# Define a type variable
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """Return the value associated with the key in the dictionary, or the default value if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
