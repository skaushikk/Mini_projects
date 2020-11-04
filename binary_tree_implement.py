# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal(root):
    if root:
        print('preorder : ' + root.data)
        tree_traversal(root.left)

        print('inorder : ' + root.data)
        tree_traversal(root.right)

        print('postorder : ' + root.data)


""" Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""


def in_order_traversal(root):
    elements = []
    if root.left:
        elements += in_order_traversal(root.left)

    elements.append(root.data)

    if root.right:
        elements += in_order_traversal(root.right)

    return elements


def post_order_traversal(root):
    elements = []
    if root.left:
        elements += post_order_traversal(root.left)
    if root.right:
        elements += post_order_traversal(root.right)

    elements.append(root.data)

    return elements


def pre_order_traversal(root):
    elements = [root.data]
    if root.left:
        elements += pre_order_traversal(root.left)
    if root.right:
        elements += pre_order_traversal(root.right)

    return elements


# Iterative Method to print the height of binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

        # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        d_left = maxDepth(root.left)
        d_right = maxDepth(root.right)

        if d_left > d_right:
            return d_left + 1
        else:
            return d_right + 1


def right_side_view(root):
    def helper(node, r_dict, depth=0):
        if not node:
            return node
        r_dict[depth] = node.data
        if node.left:
            helper(node.left, r_dict, depth + 1)
        if node.right:
            helper(node.right, r_dict, depth + 1)
        return r_dict

    r_dict, ar, k = {}, [], 0
    helper(root, r_dict)
    while k in r_dict:
        ar.append(r_dict[k])
        k += 1
    return ar


def average_at_depth(root):
    def helper(node, r_dict, depth=0):
        if not node:
            return node
        if depth not in r_dict:
            r_dict[depth] = [0, 0]
        r_dict[depth][0].append('____' + node.data)
        r_dict[depth][1] += 1
        if node.left:
            helper(node.left, r_dict, depth + 1)
        if node.right:
            helper(node.right, r_dict, depth + 1)
        return r_dict

    r_dict, ar, k = {}, [], 0
    helper(root, r_dict)
    while k in r_dict:
        # ar.append(r_dict[k][0]/r_dict[k][1])
        print(r_dict[k][0], r_dict[k][1])
        k += 1
    return ar


from collections import deque


def printLevelOrder(root):
    # Base Case
    if root is None:
        return

        # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


""" bfs traverse tree and accumulate nodes by levels"""

from collections import deque


def bfs_levels_accumulate(root):
    if root is None:
        return root

    q = deque()
    q.append(root)
    level = 0

    levels = {}

    while q:
        node = q.popleft()
        if level not in levels:
            levels[level] = []
        levels[level] = node.data

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
        level += 1

    return levels


import collections


def lowest_common_ancestor(root, node1, node2):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def helper(root, node1, node2):
        if not root:
            return Status(0, None)

        left_result = helper(root.left, node1, node2)
        if left_result.num_target_nodes == 2:
            return left_result

        right_result = helper(root.right, node1, node2)
        if right_result.num_target_nodes == 2:
            return right_result

        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes + int(root is node1) + int(
            root is node2))
        return Status(num_target_nodes, root if num_target_nodes == 2 else None)

    return helper(root, node1, node2).ancestor


def lowestCommonAncestor(root, p, q):
    ans = root
    def recurse_tree(current_node):
        nonlocal ans
        # If reached the end of a branch, return False.
        if not current_node:
            return False

        # Left Recursion
        left = recurse_tree(current_node.left)

        # Right Recursion
        right = recurse_tree(current_node.right)

        # If the current node is one of p or q
        mid = current_node == p or current_node == q

        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            ans = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right

    # Traverse the tree
    recurse_tree(root)
    return ans.data


def is_balanced_binary_tree(tree):
    BalancedStatuswithHeight = collections.namedtuple(
        'BalancedStatuswithHeight', ('balanced', 'height'))

    # First vaTue of the return value indicates i.f tree js baTanced, and if
    # baTanced the second value of the return vaTue is tie height of tree,
    def check_balanced(tree):

        if not tree:
            return BalancedStatuswithHeight(True, -1)  # Base case.
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced.
            return BalancedStatuswithHeight(False, 0)
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced.
            return BalancedStatuswithHeight(False, 0)
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatuswithHeight(is_balanced, height)

    return check_balanced(tree).balanced


def main():
    H = TreeNode("H")
    G = TreeNode("G", H)
    F = TreeNode("F", None, G)
    D = TreeNode("D")
    E = TreeNode("E")
    C = TreeNode("C", D, E)
    B = TreeNode("B", C, F)

    M = TreeNode("M")
    L = TreeNode("L", None, M)
    N = TreeNode("N")
    K = TreeNode("K", L, N)
    P = TreeNode("P")
    O = TreeNode("O", None, P)
    J = TreeNode("J", None, K)
    I = TreeNode("I", J, O)

    A = TreeNode("A", B, I)

    # tree_traversal(A)
    print('preorder traversal', pre_order_traversal(A))
    print('inorder traversal', in_order_traversal(A))
    print('postorder traversal', post_order_traversal(A))

    printLevelOrder(A)
    # print(maxDepth(A))
    print(right_side_view(A))
    # print(average_at_depth(A))
    # print(printLevelOrder(A))

    levels = bfs_levels_accumulate(A)
    print(levels)
    # for k in levels:
    #     print(levels[k])
    print(is_balanced_binary_tree(A))
    print(lowest_common_ancestor(A, E, G).data)
    print(lowestCommonAncestor(A, B, P))

if __name__ == "__main__":
    main()

    # stack = []
    #
    # stack.append((5,5))
    # stack.append("c")
    # print(stack)
