#!/usr/bin/python3
""" LIFO Caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """
    
    LAST_INSERTED_KEYS = []
    
    def put(self, key: str, item: str) -> None:
        """put into cache using first in first out alogorithm"""
        if not key or not item:
            return
        LIFOCache.LAST_INSERTED_KEYS.append(key)
        self.cache_data[key] = item
        if self.MAX_ITEMS < len(self.cache_data.items()):
            print(f"DISCARD: {LIFOCache.LAST_INSERTED_KEYS[-2]}")
            del self.cache_data[LIFOCache.LAST_INSERTED_KEYS[-2]]

    def get(self, key: str) -> str:
        """gets by key sepecifiec item from cache data"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
