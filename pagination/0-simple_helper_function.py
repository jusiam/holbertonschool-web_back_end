#!/usr/bin/env python3
"""
Main file
"""


def index_range(page, page_size):
    """result"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
