"""
buid a general tree data structure
"""


class TreeNode(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, max_level):
        space = ' ' * self.get_level() * 3
        if self.get_level() <= max_level:
            if self.get_level() != 0:
                space = space + "|__ "
            print(space + self.name)
        if self.children:
            for child in self.children:
                child.print_tree(max_level)


def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Windows'))
    laptop.add_child(TreeNode('Chromebook'))

    root.add_child(laptop)
    root.print_tree()
    # print(root.get_level())
    return root


def build_management_tree():
    root = TreeNode('World')

    l1 = TreeNode('India')
    l2 = TreeNode('USA')

    l11 = TreeNode('Gujarat')
    l12 = TreeNode('Karnataka')

    l111 = TreeNode('Ahmedabad')
    l112 = TreeNode('Baroda')

    l121 = TreeNode('Bangaluru')
    l122 = TreeNode('Mysore')

    l21 = TreeNode('New Jersey')
    l22 = TreeNode('California')
    l211 = TreeNode('Princeton')
    l212 = TreeNode('Trenton')
    l221 = TreeNode('San Francisco')
    l222 = TreeNode('Mountain View')
    l223 = TreeNode('Palo Alto')

    root.add_child(l1)
    root.add_child(l2)
    l1.add_child(l11)
    l1.add_child(l12)
    l11.add_child(l111)
    l11.add_child(l112)
    l12.add_child(l121)
    l12.add_child(l122)
    l2.add_child(l21)
    l2.add_child(l22)
    l21.add_child(l211)
    l21.add_child(l212)
    l22.add_child(l221)
    l22.add_child(l222)
    l22.add_child(l223)
    return root


if __name__ == '__main__':
    # build_product_tree()
    root = build_management_tree()
    root.print_tree(3)
