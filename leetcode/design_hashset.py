"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:
    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist
        in the HashSet, do nothing.

 

Example 1:
    Input
    ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output
    [null, null, null, true, false, null, true, null, false]

    Explanation
    MyHashSet myHashSet = new MyHashSet();
    myHashSet.add(1);      // set = [1]
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(1); // return True
    myHashSet.contains(3); // return False, (not found)
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(2); // return True
    myHashSet.remove(2);   // set = [1]
    myHashSet.contains(2); // return False, (already removed)

Constraints:
    0 <= key <= 10^6
    At most 10^4 calls will be made to add, remove, and contains.

A:
    contains on empty -> return False
    add already there -> don't add - or just replace
    remove not there  -> do nothing
    all keys are integers so can hash by key itself
"""


class MyHashSet:
    def __init__(self):
        self.hash = [None for _ in range(10**6 + 1)]

    def add(self, key: int) -> None:
        self.hash[key] = key

    def remove(self, key: int) -> None:
        self.hash[key] = None

    def contains(self, key: int) -> bool:
        return True if self.hash[key] is not None else False


cases = [
    (
        [
            "MyHashSet",
            "add",
            "add",
            "contains",
            "contains",
            "add",
            "contains",
            "remove",
            "contains",
        ],
        [[], [1], [2], [1], [3], [2], [2], [2], [2]],
    ),
    (
        [
            "MyHashSet",
            "add",
            "remove",
            "add",
            "remove",
            "remove",
            "add",
            "add",
            "add",
            "add",
            "remove",
        ],
        [[], [9], [19], [14], [19], [9], [0], [3], [4], [0], [9]],
    ),
]

obj = MyHashSet()
for (cmds, keys) in cases:
    for (cmd, key) in zip(cmds, keys):
        if cmd == "MyHashSet":
            continue

        key = key[0]
        func = getattr(obj, cmd)
        ans = func(key)

        if cmd == 'add':
            if key:
                assert obj.hash[key] == key
            continue
        if cmd == 'contains':
            if key in obj.hash:
                assert ans
            else:
                assert not ans
            continue
        if cmd == 'remove':
            assert not obj.hash[key]
            continue
