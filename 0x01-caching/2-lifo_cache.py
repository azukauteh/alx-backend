#!/usr/bin/python3
"""LIFO Cache Replacement Implementation Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    An implementation of LIFO (Last In First Out) Cache Replacement Policy
    """

    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            with self.__rlock:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    """ If cache is full, discard the last item (LIFO)"""
                    discarded_key = self.__keys.pop()
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
                self.cache_data[key] = item
                self.__keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        with self.__rlock:
            return self.cache_data.get(key, None)
