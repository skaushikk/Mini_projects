"""
building a stack data structure class
"""
import timing


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return

    @property
    def show_stack(self):
        return self.items

    def reverse_stack(self):
        if self.is_empty():
            return
        s = Stack()

        while not self.is_empty():
            s.push(self.pop())
        return s


# s = Stack()
# s.push(5)
# s.push(4)
# s.push(-4)
# s.push(1)
# s.push(2)
# s.push(10)
# print(s.show_stack())
# s.pop()
# print(s.show_stack())
# print(s.reverse_stack().show_stack())

inputstring = 'Hello'
s = Stack()
for i in inputstring:
    s.push(i)
print(s.show_stack)
# print(s.reverse_stack().show_stack())
rev = ''
while not s.is_empty():
    rev += s.pop()
    # print(rev)
print(rev)
