"""
given a binary tree, calculate teh average of numbers at each depth
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def append


def _collect(node, _dict, depth=0):
    if not node:
        return node
    if depth not in _dict:
        _dict[depth].append(node.val)

    _collect(node.left. _dict, depth+1)
    _collect(node.right, _dict, depth+1)

def _traverse(node):
    data = {}
    _collect(node, data)
    result = []
    while i in data:
        nums = data[i]
        avg = sum(nums)/len(nums)
        result.append(avg)
        i+=1

    return result
