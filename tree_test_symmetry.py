from binary_tree_implement import *
import _collections

def main():
    E1 = TreeNode('E')
    E2 = TreeNode('E')
    F1 = TreeNode('F')
    F2 = TreeNode('F')
    C1 = TreeNode('C', E1, None)
    C2 = TreeNode('C', None, E2 )
    D1 = TreeNode('D',  None, F1)
    D2 = TreeNode('D', F2, None )
    B1 = TreeNode('B', C1, D1)
    B2 = TreeNode('B', D2, C2 )
    A = TreeNode("A", B1, B2)

    # tree_traversal(A)
    print('preorder traversal', pre_order_traversal(A))
    print('inorder traversal', in_order_traversal(A))
    print('postorder traversal', post_order_traversal(A))
    print(isSymmetric(A))
    print(isSymmetric_iter(A))
    print(isSymmetric_bfs(A))



#dfs recursive

def isSymmetric(root):
    def dfs(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.data == right.data:
            outer = dfs(left.left, right.right)
            inner = dfs(left.right, right.left)
            return outer and inner
        else:
            return False
    if root is None:
        return True
    else:
        return dfs(root.left, root.right)


#dfs iteration stacks

def isSymmetric_iter(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True

    stack = []
    stack.append((root.left, root.right))

    while len(stack):
        l, r = stack.pop()
        if l is None and r is None:
            continue
        # if (not l and r) or (l and not r) or (l.data != r.data):
        if not l or not r:
            return False
        if l and r:
            print(l.data, r.data)
        if l.data != r.data:
            return False
        stack.append((l.right, r.left))
        stack.append((l.left, r.right))

    return True


# bfs iteration deque

def isSymmetric_bfs(root):
    if not root:
        return True
    if root.left is None and root.right is None:
        return True

    q = collections.deque()
    q.append((root.left, root.right))

    while len(q):
        l, r = q.popleft()
        if l is None and r is None:
            continue
        if not l or not r:
            return False
        if l and r:
            print(l.data, r.data)
        if r.data != l.data:
            return False
        q.append((l.right, r.left))
        q.append((l.left, r.right))
    return True


if __name__ == '__main__':
    main()