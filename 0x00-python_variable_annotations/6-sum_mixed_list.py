#!/usr/bin/env python3
"""Returns sum of list of intergers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums and return list, mxd_lst"""
    return sum(mxd_lst)
