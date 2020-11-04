"""
Use stacks to convert integer to binary

242

242/2 = 121 -->0
121/2 = 60  -->1
60/2 = 30   -->0
30/2 = 15   -->0
15/2 = 7    -->1
7/2 = 3   -->1
3/2 = 1   -->1
1/2 = 0 --->1

11110010
"""
from stack import Stack
import timing

def int2bin(num):
    s = Stack()

    n = num
    x = True
    while x:
        div  = n // 2
        rem = n % 2
        s.push(rem)
        n = div
        if div == 0:
            x = False

    bin_num = ''
    while not s.is_empty:
        bin_num = bin_num+str(s.pop())
    return bin_num


print(int2bin(242))
