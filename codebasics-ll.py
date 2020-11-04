'''
File: d:\My Projects\ML\kaushik_projects\Repos\Courses\Data Sructures\codebasics.py
Project: d:\My Projects\ML\kaushik_projects\Repos\Courses\Data Sructures
Created Date: Thursday September 3rd 2020
Author: skaushikk
-----
Last Modified:
Modified By:
-----
Copyright (c) 2020 Your Company
'''
import timing 

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node =Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr  += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count

    def remove_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')

        if index==0:
            self.head = self.head.next
            return
        
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr=itr.next
            count+=1

def even_odd_merge(head):
    if not head:
        return head
    even_dummy_head, odd_dummy_head = Node(0), Node(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while head:
        tails[turn].next = head
        head = head.next
        tails[turn] =tails[turn].next
        turn ^= 1
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next

def odd_even_merge(head):
    if not head:
        return head
    odd = head
    even = head.next
    evenhead = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenhead
    return head
    

if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(67)
    # ll.insert_list(["mangoes","bananas","apples","oranges",'pecans'])
    # ll.print()
    # ll.remove_at(2)
    # ll.print()
    for i in range(1,11):
        ll.insert_at_end(i)
    ll.print()
    head = ll.head
    even_odd_merge(head)
    ll.print()
    odd_even_merge(head)
    ll.print()
    
