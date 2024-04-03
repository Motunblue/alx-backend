#!/usr/bin/env python3
"""Basic Cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache"""

    def put(self, key, item):
        """Put item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get items from cache"""
        return self.cache_data.get(key)
