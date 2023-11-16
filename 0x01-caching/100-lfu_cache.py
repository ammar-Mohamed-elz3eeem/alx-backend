#!/usr/bin/python3
""" LFU Caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """Initializes LFUCache object"""
        super().__init__()
        self.keys = []
        self.used = {}

    def put(self, key: str, item: str) -> None:
        """put into cache using first in first out alogorithm"""
        if not key or not item:
            return
        if (len(self.keys) == BaseCaching.MAX_ITEMS and key not in self.keys):
            item_to_remove = self.keys.pop(self.keys.index(self.findLFU()))
            del self.cache_data[item_to_remove]
            del self.used[item_to_remove]
            print(f"DISCARD: {item_to_remove}")
        self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)
            self.used[key] = 0
        else:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.used[key] += 1

    def get(self, key: str) -> str:
        """gets by key sepecifiec item from cache data"""
        if not key or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        self.used[key] += 1
        return self.cache_data.get(key)

    def findLFU(self):
        items = list(self.used.items())
        freq = [item[1] for item in items]
        least = min(freq)

        lkeys = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lkeys:
                return key
