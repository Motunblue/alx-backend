#!/usr/bin/env python3
""" LRU Caching"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache"""

    def __init__(self):
        """Initialization"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.count = 0

    def put(self, key, item):
        """Put item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=True)
                return
            if self.count == BaseCaching.MAX_ITEMS:
                x, _ = self.cache_data.popitem(last=False)
                self.count -= 1
                print("DISCARD: " + x[0])
            self.cache_data[key] = item
            self.count += 1

    def get(self, key):
        """Get items from cache"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
