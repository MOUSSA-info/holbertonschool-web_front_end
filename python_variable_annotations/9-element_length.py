#!/usr/bin/env python3
"""Function that returns a list of tuples with elements and their lengths."""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple is (element, length of element).
    
    Parameters:
    - lst: an iterable of sequences (e.g., list of strings, list of lists).
    
    Returns:
    - list of tuples (sequence, int)
    """
    return [(i, len(i)) for i in lst]

