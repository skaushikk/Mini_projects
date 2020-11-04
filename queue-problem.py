"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

"""

from collections import deque
from time import sleep, time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if self.is_empty:
            return print('The Q is empty!')
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

# p = Queue()
#
# def place_o(orders):
#     for order in orders:
#         print('Placing the orders')
#         p.enqueue(order)
#         sleep(0.5)
#
# def serve_o():
#     sleep(1)
#     while True:
#         order = p.dequeue()
#         print('Now Serving: ', order)
#         sleep(2)
#
# if __name__ == '__main__':
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     t1 = threading.Thread(target=place_o, args=(orders,))
#     t2 = threading.Thread(target=serve_o)
#
#     t1.start()
#     t2.start()

    def front(self):
        return self.buffer[-1]


def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", numbers_queue)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)
