class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(-1)
        else:
            return

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '[' and p2 == ']':
        return True
    if p1 == '{' and p2 == '}':
        return True


def isValid(string):
    if len(string)%2 != 0:
        return False
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(string) and is_balanced:
        paren = string[index]
        if paren in '([{':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


string = "([]{(})"
print(isValid(string))