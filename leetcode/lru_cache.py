"""Design and implement a data structure for Least Recently Used (LRU) cache. It should support
the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. When the cache
reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LRUCache:
    import time as t

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.cache[key] = (self.t.time(), self.cache[key][1])
        return self.cache[key][1]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.cache) < self.capacity or key in self.cache:
            self.cache[key] = (self.t.time(), value)

        else:
            minTime = float('inf')
            for k in self.cache:
                if self.cache[k][0] < minTime:
                    minTime = self.cache[k][0]
                    minKey = k
            del self.cache[minKey]
            self.cache[key] = (self.t.time(), value)

    def print(self, s):
        print(s)
        print(self.cache)
        print('-----------------------')


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache(2)

cache.get(2)
cache.put(2, 6)
cache.print('added (2,6)')
cache.get(1)
cache.put(1, 5)
cache.print('added (1,5)')
cache.put(1, 2)
cache.print('added (1,2)')
cache.get(1)
cache.get(2)
