#!/usr/bin/env python3
"""Simple function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Return tuple contating start index and end idx of a page"""
    return ((page - 1) * page_size, page_size * page)
