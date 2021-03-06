def averageOfLevels(self, root):
    # In case the tree is empty (you never know :P)
    if root is None:
        return

    # Create the queue for BFS and the list of averages
    queue = []
    averages = []

    # Enqueue Root and initialize nodes_count_per_level and sum_per_level
    queue.append(root)
    nodes_count_per_level = 0
    sum_per_level = 0

    # Append None as the root is alone
    queue.append(None)

    # BFS
    while(len(queue) > 0):
        node = queue.pop(0)
        if node is None:
            averages.append(sum_per_level / nodes_count_per_level)
            sum_per_level = 0
            nodes_count_per_level = 0
            queue.append(None)

            if queue[0] is None:
                break
            else:
                continue

        #
        sum_per_level += node.val
        nodes_count_per_level += 1

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
    return averages