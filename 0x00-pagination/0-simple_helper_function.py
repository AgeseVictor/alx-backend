#!/usr/bin/env python3
"""The function return a tuple of size two i.e. pagination parameters"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''return a tuple of size two:pagination parameters'''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
