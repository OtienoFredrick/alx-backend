#!/usr/bin/env python3
"""
Create a class LRUCache that inherits
from BaseCaching and is a caching system:

You must use self.cache_data - dictionary
from the parent class BaseCaching
You can overload def __init__(self): but don’t
forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the
item value for the key key.If key or item is None,
this method should not do anything.
If the number of items in self.cache_data is higher
that BaseCaching.MAX_ITEMS: you must discard the least
recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and
following by a new line def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Defines methods for Least Recently
    Used Caching
    """

    def __init__(self):
        """
        Defines init constructor to inherit
        from the main class
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        puts method to impliment LRU
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                     self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        Get method
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
