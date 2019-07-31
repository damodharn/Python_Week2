# *********************************************************************************************
# Purpose: To write a program to Find prime Anagram nos up to range 1000 and storing them in Queue using Link List.
# Author:  Damodhar D. Nirgude.
# **********************************************************************************************
from Anagram_Stack import Prime_Anagram
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.cnt = 0
        self.size = 100

    #  *****************************  Method to insert item at rear into the List  ***********************

    def enqueue(self, data):
        if self.front is None:  # If Queue is empty insert element at front else after the last node
            self.front = Node(data)  # and update the rear with last node added.
            self.rear = self.front
            self.cnt += 1
        else:
            temp = Node(data)
            self.rear.next = temp
            self.rear = temp
            self.cnt += 1

    # **************************  Method to remove item from Queue Front  ***********************

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty...Can't De-Queue item")
        else:
            item = self.front.data
            self.front = self.front.next
            self.cnt -= 1
            return item

    # ***********************************  Method to check is Queue is Empty or Not ********************

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def is_full(self):
        if self.cnt == self.size:
            return True
        else:
            return False

    def size_queue(self):
        return self.cnt
# ##############################################  MAIN Method  #######################################################


def main():
    cnt = 0
    qq = Queue()
    pa = Prime_Anagram()
    ar = pa.anagram(pa.primeno())
    start_time = time.time()
    print("Inserting data into the Queue...")
    while (time.time() - start_time) < 1:
        continue
    for i in ar:
        if qq.is_full() is False:
            qq.enqueue(i)
        else:
            print("Queue is Full...Can't Insert item")
            break
    print("\nData Added to the Queue\n\nSize of a Queue: ", qq.size_queue())
    start_time = time.time()
    while (time.time() - start_time) < 1:
        continue
    print("\nPrinting Anagram No from the Queue:...")
    print("__________________________________________________________________________________________________")
    start_time = time.time()
    while (time.time() - start_time) < 1:
        continue
    while True:
        if qq.is_empty() is False:
            cnt += 1
            if cnt % 15 == 0:
                print(qq.dequeue())
            else:
                print(qq.dequeue(), end=" ")
        else:
            print("\nQueue is Empty ")
            break
    print("\nSize of Queue after Dequeing data from Queue: ", qq.size_queue())


if __name__ == "__main__":
    main()