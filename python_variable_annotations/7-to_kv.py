#!/usr/bin/env python3
"""Function that returns a tuple of (string, square of number as float)."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is the string `k`,
    and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))

