"""
Cracking hte coding interview- solutions
"""

"""
# 1.5
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false 
"""

def one_away(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l1 == l2:
        test = check_replaced(s1, s2)
    if l1 > l2:
        test = check_removed(s1, s2)
    if l1 < l2:
        test = check_removed(s2, s1)
    return test
def check_removed(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            same = True
        else:
            i += 1
            same = False

    return same

def check_replaced(s1, s2):
    k = 0
    test = False
    i = 0
    while i < len(s1) and k <= 1:
        if s1[i] == s2[i]:
            i += 1
            test = True
        else:
            k += 1
            i += 1
        if k > 1:
            return False
    return test

s1 = 'pease'
s2 = 'pease'
print(one_away(s1, s2))




