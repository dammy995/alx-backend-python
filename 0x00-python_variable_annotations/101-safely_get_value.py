#!/usr/bin/env python3
""" return values, add type annotations to the function"""
from typing import Mapping, TypeVar, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return dct[key] or default value"""
    if key in dct:
        return dct[key]
    else:
        return default
