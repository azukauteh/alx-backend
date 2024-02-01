#!/usr/bin/python3
"""LFU Cache Replacement Implementation Class
"""
from threading import RLock

LFUCache = __import__('100-lfu_cache').LFUCache



class LFUCache(BaseCaching):
    """
    An implementation of LFU (Least Frequently Used) Cache Replacement Policy
    """

    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__stats = {}
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        with self.__rlock:
            if key in self.cache_data:
                """ If key already exists, update its value"""
                self.cache_data[key] = item
            else:
                """ If key doesn't exist, check if cache is full"""
                if len(self.cache_data) >= self.MAX_ITEMS:
                    """ If cache is full, discard the least frequently used
                    item (LFU)"""
                    min_count = min(self.__stats.values())
                    keys_to_discard = [k for k, v in self.__stats.items()
                                       if v == min_count]
                    if len(keys_to_discard) > 1:
                        """ If there are multiple keys with the same least
                           frequency use LRU to discard"""
                        discarded_key = self._balance(keys_to_discard)
                    else:
                        """ Otherwise, discard the single least frequently
                        used key"""
                        discarded_key = keys_to_discard[0]
                    del self.cache_data[discarded_key]
                    del self.__stats[discarded_key]

                """ Update cache data with the new key and item"""
                self.cache_data[key] = item
                self.__stats[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        with self.__rlock:
            if key in self.cache_data:
                """ If key exists, update its frequency count and
                return its value"""
                self.__stats[key] += 1
                return self.cache_data[key]
            else:
                return None

    def _balance(self, keys_to_discard):
        """ Balance the cache by discarding the least recently used
        key from the provided list of keys
        """
        """ We use LRU algorithm to discard the least recently used
        key from the list"""
        return min(keys_to_discard, key=lambda k: self.__stats[k])
