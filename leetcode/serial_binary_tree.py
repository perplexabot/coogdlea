"""Given the root to a binary tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'`
"""
import re
import math
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize_tree(serial):
    def get_deliminators(serial):
        delim_pattern = r'^(.*)(.*?)\1(.*?)\1'
        delim_regex = re.compile(delim_pattern, re.DOTALL)
        deliminator_tuple = delim_regex.findall(serial)[0]
        return deliminator_tuple

    root = None
    delim_delim, val_delim, childless_delim = get_deliminators(serial)
    full_tree_count = serial.count(val_delim)
    levels = int(math.log(full_tree_count, 2)//1)

    # move index to begining of data
    index = len(delim_delim)*3 + len(val_delim) + len(childless_delim)

    # read data, create nodes and add them into a list of lists depending on
    # which level it belongs
    all_level_nodes = []
    for i in range(levels+1):
        level_nodes = []
        for j in range(2**i):
            end = index+1
            while end < len(serial) and not serial[end].startswith(val_delim):
                end += 1
            val = '' if val_delim in serial[index:end] else serial[index:end]
            level_nodes.append(Node(val) if val != childless_delim else childless_delim)
            index = index + 1 if val_delim in serial[index:end] else end + len(val_delim)
        all_level_nodes.append(level_nodes)

    # connect parents to children
    i = 0

    while i < len(all_level_nodes) - 1:
        cnt = 0
        for nd in all_level_nodes[i]:
            if nd != childless_delim:
                nd.left=all_level_nodes[i+1][cnt] if all_level_nodes[i+1][cnt] != childless_delim else None
                nd.right=all_level_nodes[i+1][cnt+1] if all_level_nodes[i+1][cnt+1] != childless_delim else None
                cnt += 2
            else:
                cnt += 1
        i += 1

    # set leave children to None
    for nd in all_level_nodes[-1]:
        if nd != childless_delim:
            nd.left = None
            nd.right = None

    return all_level_nodes[0][0]

def serialize_tree(head):
    """serialize tree given head. Returns a string."""
    def get_dictionary_from_tree(head):
        dictionary = set()
        Q = deque([head])
        while Q:
            current_node = Q.popleft()
            dictionary.add(current_node.val)
            if current_node.left:
                Q.append(current_node.left)

            if current_node.right:
                Q.append(current_node.right)
        return dictionary

    # TODO: can get a way with only using 2 delims.
    def get_delims(head, dictionary, count=1):
        """find unique delimators, given tree head and a dictionary of the data words
        returns count number of deliminators"""
        # Assuming input data set will never contain all utf-8 chars (up to N - count utf-8 chars
        # can be in the data. If this assumption fails, then this function needs to expand to
        # create deliminators of length greater than 1) in one tree.

        found = []
        point_list = [ord(char) for word in dictionary for char in word]
        point_list.sort()
        # check for unused characters in utf-8 between used chars. 
        ind = 0
        while len(found) < count and ind < len(point_list)-1:
            if point_list[ind+1] - point_list[ind] > 1:
                offset = 1
                while point_list[ind] + offset < point_list[ind+1] and len(found) < count:
                    found.append(chr(point_list[ind] + offset))
                    offset += 1
            ind += 1

        # gather remaining unused chars by offseting from last (greatest point value) char used
        base = point_list[-1] if point_list else ord('#') - 1
        offset = 1
        while len(found) < count:
            found.append(chr(base + offset))
            offset += 1
        return tuple(found)

    dictionary = get_dictionary_from_tree(head)
    val_delim, childless_delim, delim_delim = get_delims(head, dictionary, count=3)
    serial = ''.join([delim_delim, val_delim,
                      delim_delim,
                      childless_delim,
                      delim_delim,
                      head.val,
                      val_delim])
    Q = deque([head])
    while Q:
        current_node = Q.popleft()
        if current_node.left:
            serial += ''.join([current_node.left.val, val_delim])
            Q.append(current_node.left)
        else:
            serial += ''.join([childless_delim, val_delim])

        if current_node.right:
            serial += ''.join([current_node.right.val, val_delim])
            Q.append(current_node.right)
        else:
            serial += ''.join([childless_delim, val_delim])
    return serial

def print_tree(head):
    Q = deque([head])
    while Q:
        curr = Q.popleft()
        print("{}\n".format(curr.val))
        if curr.left:
            Q.append(curr.left)
        if curr.right:
            Q.append(curr.right)


NODES = [Node('root', Node('left', Node('left.left')), Node('right')),
         Node(u'\57', Node('left' + u'\57', Node(u'\66'), Node(u'\67')), Node('')),
         Node(u'\59')]

for NODE in NODES:
    print("Tree in question: ")
    print_tree(NODE)
    serial = serialize_tree(NODE)
    print("serial : ", serial)
    head = deserialize_tree(serial)
    print("Deserialized tree: ")
    print_tree(head)
    print('-----------------------------')
