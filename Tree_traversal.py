"""
in order traversal
"""

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None



def inorderTraversal_dfs(root):
    if root is None:
        return None
    res = []
    def dfs (root, res):
        if root:
            res.append(dfs(root.left, res))
            res.append(root.val)
            res.append(dfs(root.right, res))
     dfs(root, res)
    return res

node = TreeNode()
