#!/usr/bin/env python3
"""
a class LIFOCache that inherits from BaseCaching
and is a caching system:
You must use self.cache_data - dictionary from the
parent class BaseCaching
You can overload def __init__(self): but don’t forget
to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the
item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and
following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache class defining methods for LIFO caching
    """

    def __init__(self):
        """
        initializes instances of the super class
        """
        super().__init__()

    def put(self, key, item):
        """
        returns nothing when key or item is None
        then determines if the size of the dictionary is greater
        than the MAX_ITEMS and deletes the last item added
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data.keys():
                # Delete the last item of the disctionary
                last_key, last_value = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        If key is None or key is not in self.cache_date.keys()
        it returns None otherwise it returns the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)
