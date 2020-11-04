"""
buid a general tree data structure
"""

class TreeNode(object):
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.parent =None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level=0
        p= self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self, ptype):
        space = ' '*self.get_level()*3
        if self.get_level()!=0:
            space = space+"|__ "
        if ptype == 'name':
            print(space + self.name)
        elif ptype == 'desig':
            print(space + self.designation)
        else:
            print(space + self.name + '({})'.format(self.designation))
        if self.children:
            for child in self.children:
                child.print_tree(ptype)

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
    root = TreeNode('Nilupul', 'CEO')
    
    l11 = TreeNode('Chinmay', 'CTO')
    l12 = TreeNode('Gels', 'HR Head')
    
    l21 = TreeNode('Vishwa', 'Infrastructure Head')
    l21.add_child(TreeNode('Dhaval', 'Cloud Manager'))
    l21.add_child(TreeNode('Abhijit', 'App Manager'))
    l22 = TreeNode('Aamir', 'Application Head')
    l12.add_child(TreeNode('Peter','Recruitment Manager'))
    l12.add_child(TreeNode('Waqas', 'Policy Manager'))
    
    root.add_child(l11)
    root.add_child(l12)
    l11.add_child(l21)
    l11.add_child(l22)
    root.print_tree('desig')
    
if __name__ == '__main__':
    # build_product_tree()
    build_management_tree()
