#!/usr/bin/env python3
"""
Main file
"""


import csv
from math import ceil
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """result"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = []
        with open('Popular_Baby_Names.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        start_index, end_index = index_range(page, page_size)
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """result"""
        page_data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = ceil(total_data / page_size)

        return {
                'page_size': len(page_data),
                'page': page,
                'data': page_data,
                'next_page': page + 1 if page < total_pages else None,
                'prev_page': page - 1 if page != 1 else None,
                'total_pages': total_pages
        }
