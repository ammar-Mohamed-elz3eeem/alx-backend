#!/usr/bin/python3
""" LRU Caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        super().__init__()
        self.order = OrderedDict()

    def put(self, key: str, item: str) -> None:
        """put into cache using first in first out alogorithm"""
        if not key or not item:
            return
        self.order[key] = item
        self.order.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item = next(iter(self.order))
            del self.cache_data[item]
            print(f"DISCARD: {item}")

        if len(self.order) > BaseCaching.MAX_ITEMS:
            self.order.popitem(False)

    def get(self, key: str) -> str:
        """gets by key sepecifiec item from cache data"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
