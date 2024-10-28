#!/usr/bin/env python3
"""
A function named  index_range that takes
two integer arguments page and page_size and
returns a tuple of size two containing a start
index and an end index corresponding to the range
of indexes to return in a list for those particular
pagination parameters
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and
    end index
    """
    # Ideas
    # if page is 1, start at 0 and end at page_size
    # if page is 2, start at (page - 1 * page_size)
    # and end at (page_size * page)
    # if page is 3, start at ((page - 1) * page_size)
    # and end at (page_size * page)
    return ((page - 1) * page_size, page_size * page)
