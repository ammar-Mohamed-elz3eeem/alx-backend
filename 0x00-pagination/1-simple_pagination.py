import csv
import math
from typing import List


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
        assert type(page) is int
        assert page > 0
        assert type(page_size) is int
        assert page_size > 0
        tup = index_range(page, page_size)
        data = self.dataset()
        return data[tup[0]:tup[1]]


def index_range(page, page_size):
    """
    function that gets starting result No and
    end Result number for pagination
    """
    return ((page - 1) * page_size, page * page_size)
