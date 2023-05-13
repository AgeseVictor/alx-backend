#!/usr/bin/python3
""" LFUCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - inherits from BaseCaching and is a caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.count = {}

    def put(self, key, item):
        """assign to the {} self.cache_data the item value for the key
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                orderkeys = self.cache_data.keys()
                ordercount = self.count.keys()
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.count[key] += 1
                else:
                    self.cache_data[key] = item
                    self.count[key] = 1
                tkeys = [(key, self.cache_data[key]) for key in orderkeys]
                self.cache_data = OrderedDict(tkeys)
                tcount = [(key, self.count[key]) for key in ordercount]
                self.count = OrderedDict(tcount)

            else:
                if key not in self.cache_data:
                    minkey = min(self.count, key=self.count.get)
                    del self.cache_data[minkey]
                    print("DISCARD: {}".format(minkey))
                    del self.count[minkey]
                    self.cache_data[key] = item
                    self.count[key] = 1
                else:
                    self.cache_data[key] = item
                    self.count[key] += 1

    def get(self, key):
        """return value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=True)
        self.count[key] += 1
        self.cache_data.move_to_end(key, last=True)
        return self.cache_data[key]
