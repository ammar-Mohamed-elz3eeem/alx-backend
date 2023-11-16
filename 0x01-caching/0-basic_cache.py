#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """BasicCache claass with no limits"""
    
    def put(self, key: str, item: str) -> None:
        """inserts new item on cache data"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key: str) -> str:
        """gets by key sepecifiec item from cache data"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
