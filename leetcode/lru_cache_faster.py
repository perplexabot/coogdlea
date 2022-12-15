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
    from collections import OrderedDict

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.capacity = capacity
        self.cnt = 0
        self.od = self.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cnt == self.capacity and key not in self.od:
            self.od.popitem(last=False)
            self.cnt -= 1

        if key not in self.od:
            self.cnt += 1
        else:
            self.od.move_to_end(key)
        self.od[key] = value

    def print(self, s):
        print(s, f'cnt[{self.cnt}]')
        print(' ', self.od)
        print('-----------------------')

    def clear(self):
        self.cnt = 0
        self.od = self.OrderedDict()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

cache = LRUCache(2)

cache.get(2)
cache.print("1 should be on top now")

cache.put(2, 6)
cache.print("2 added")

cache.get(1)
cache.print("1 should be on top now")

cache.put(1, 5)
cache.print("1 added")

cache.put(1, 2)
cache.print("1 added")

cache.get(1)
cache.print("1 should be on top now")

cache.get(2)
cache.print("2 should be on top now")

print('############################################################')

cache.clear()

cache.put(1, 1)
cache.print("added (1,1)")

cache.put(2, 2)
cache.print("added (2,2)")

cache.get(1)
cache.print("1 should be on top now")

cache.put(3, 3)
cache.print("added (3,3)")

cache.get(2)
cache.print("2 should be on top now")

cache.put(4, 4)
cache.print("added (4,4)")

cache.get(1)
cache.print("1 should be on top now")

cache.get(3)
cache.print("3 should be on top now")

cache.get(4)
cache.print("4 should be on top now")

print('############################################################')

cache.clear()

cache.put(2, 1)
cache.print("added (2,1)")

cache.put(2, 2)
cache.print("added (2,2)")

cache.get(2)
cache.print("2 should be on top now")

cache.put(1, 1)
cache.print("added (1,1)")

cache.put(4, 1)
cache.print("added (4,1)")

cache.get(2)
cache.print("2 should be on top now")

print('############################################################')

cache.clear()

cache.put(2, 1)
cache.print("added (2,1)")

cache.put(1, 1)
cache.print("added (1,1)")

cache.put(2, 3)
cache.print("added (2,3)")

cache.put(4, 1)
cache.print("added (4,1)")

cache.get(1)
cache.print("1 should be on top now")

cache.get(2)
cache.print("2 should be on top now")
