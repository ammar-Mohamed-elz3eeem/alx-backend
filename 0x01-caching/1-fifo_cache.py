#!/usr/bin/python3
""" FIFO Caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """
    def put(self, key: str, item: str) -> None:
        """put into cache using first in first out alogorithm"""
        if not key or not item:
            return
        self.cache_data[key] = item
        keys_in_cache = list(self.cache_data.keys())
        if self.MAX_ITEMS < len(keys_in_cache):
            print(f"DISCARD:{keys_in_cache[0]}")
            del self.cache_data[keys_in_cache[0]]

    def get(self, key: str) -> str:
        """gets by key sepecifiec item from cache data"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
