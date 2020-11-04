"""
Implementing the single linked list data structure and all the core methods
"""
import timing


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def print(self):
        cur_node = self.head
        llstr = ''
        while cur_node:
            llstr += str(cur_node.data) + " --> "
            cur_node = cur_node.next
        print(llstr)

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            prev = self.head
            cur_node = self.head.next
            i = 1
            while cur_node and i != pos:
                prev = cur_node
                cur_node = cur_node.next
                i += 1

            if cur_node is None:
                print("The position does not exit!")

            else:
                new_node.next = cur_node
                prev.next = new_node

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            print('invalid key')
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_ll(self):
        # if self.head is None:
        #     return
        prev = None
        cur_node = self.head
        _next = None

        while cur_node:
            _next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = _next
        self.head = prev

    def reverse_recursive(self):

        def _rev_recursive(cur_node, prev):
            if cur_node is None:
                return prev

            _next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = _next
            return _rev_recursive(cur_node, prev)

        self.head = _rev_recursive(cur_node=self.head, prev=None)

    def merge_ll(self, llist2):
        l1 = self.head
        l2 = llist2.head
        l3 = Node(0)

        if not l1:
            l3 = l2
        if not l2:
            l3 = l1
        if l1 and l2:
            if l1.data < l2.data:
                l3 = l1
                l1 = l1.next
            else:
                l3 = l2
                l2 = l2.next
            l3_head = l3

        while l1 and l2:
            if l1.data < l2.data:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next

            l3 = l3.next

        if l1 and not l2:
            l3.next = l1
        if l2 and not l1:
            l3.next = l2
        return l3_head

    def pair_swap_ll(self):
        node = self.head
        d = Node(-1)
        d.next = node
        tmp = d

        while d.next and d.next.next:
            first = d.next
            second = d.next.next

            d.next, first.next, second.next = second, second.next, first
            d = d.next.next
        self.head = tmp.next


llist = LinkedList()
llist2 = LinkedList()

llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.print()
llist.pair_swap_ll()
# llist.print()

# llist.swap_pairs()
llist.print()
# llist2.prepend(0)
# llist.print()
# llist.reverse_ll()
# llist.print()
# llist.insert(8, 6)
# llist.print()

# llist.swap_nodes(1,5)
# llist.print()

llist.reverse_recursive()
llist.print()
# llist.print()


# llist2.append(2)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)
# llist2.append(10)
# llist2.append(12)
# llist2.print()
# 
# llist.merge_ll(llist2)
# llist.print()
