#!/usr/bin/env python3
"""FIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache"""

    def __init__(self):
        """Initialization"""
        super().__init__()
        self.count = 0

    def put(self, key, item):
        """Put item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if self.count == BaseCaching.MAX_ITEMS:
                x = list(self.cache_data.items())[0]
                del self.cache_data[x[0]]
                self.count -= 1
                print("DISCARD: " + x[0])
            self.cache_data[key] = item
            self.count += 1

    def get(self, key):
        """Get items from cache"""
        return self.cache_data.get(key)
