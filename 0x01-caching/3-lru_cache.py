#!/usr/bin/python3
"""LRU Cache Replacement Implementation Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    An implementation of LRU (Least Recently Used) Cache Replacement Policy
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
        if key is None or item is None:
            return

        with self.__rlock:
            """ Check if the key already exists"""
            if key in self.cache_data:
                """ If key exists, update its value and move it to the end of the __keys
                list (MRU position)
                """
                self.__keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                """ If cache is full, discard the least recently used item (LRU)"""
                discarded_key = self.__keys.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            """ Update cache data and __keys list with the new key and item"""
            self.cache_data[key] = item
            self.__keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        with self.__rlock:
            if key in self.cache_data:
                """ If key exists, move it to the end of the __keys list (MRU position)"""
                self.__keys.remove(key)
                self.__keys.append(key)
                return self.cache_data[key]
            else:
                return None
