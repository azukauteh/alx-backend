#!/usr/bin/python3
"""Basic Cache implementation Class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache implementation class

    Attributes:
        cache_data: dictionary to store cached items
    """

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: key to access the item
            item: item to be cached
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key: key to access the item
        Returns:
            The cached item if found, None otherwise
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
