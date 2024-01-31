#!/usr/bin/python3
"""FIFO Cache Replacement Implementation Class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    An implementation of FIFO (First In First Out) Cache Replacement Policy
    """

    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            """ If cache is full, discard the first item (FIFO)"""
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        """ Add the new item to the cache"""
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
