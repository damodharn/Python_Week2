# *********************************************************************************************
# Purpose: To create an Utility class for Data Structure Programs
# Author:  Damodhar D. Nirgude.
# ************************************************************************************************


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#  *********************************  ORDERED LIST  *********************************************


class LinkList2:
    def __init__(self):
        self.head = None

    def insert_at(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            if self.head.data > data:
                temp = Node(data)
                temp.next = self.head
                self.head = temp
            else:
                prev = None
                temp = self.head
                while temp is not None:
                    if temp.data > data:
                        prev.next = Node(data)
                        prev.next.next = temp
                        break
                    prev = temp
                    temp = temp.next
                if temp is None:
                    temp = Node(data)
                    prev.next = temp

    def print_list(self):
        temp = self.head  # assigning head to temporary variable temp
        while temp is not None:  # traversing through list till it ends.
            print(temp.data, end=' ')
            temp = temp.next

    def pop(self):
        var = []
        while self.head is not None:
            var.append(self.head.data)
            self.head = self.head.next
        return var

    def search(self, no):
        if self.head.data == no:  # If No. found in head
            self.head = self.head.next  # Updating head with Next Node.
        else:
            temp = self.head
            prev = None
            while temp is not None and temp.data <= no:  # Traversing through List till last or upto the no
                # greater then User i/p no.
                if temp.data == no:  # if no found in any Node
                    prev.next = temp.next  # Bypassing that node i,e Deleting that Node.
                    break
                prev = temp
                temp = temp.next
            if temp is None:
                temp = Node(no)
                prev.next = temp
            elif temp.data > no:  # If No not found till last or if we got No greater than i/p no
                #  Inserting the New Node at that place
                prev.next = Node(no)
                prev.next.next = temp


#  **************************************  UNORDERED LINK LIST  ***************************************


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        if self.last is None:  # Checking if already node present or not.
            self.head = Node(data)  # Creating a node if list is empty.
            self.last = self.head
        else:
            self.last.next = Node(data)  # Adding node after last node
            self.last = self.last.next

    def insert_rev(self, data):
        if self.last is None:  # Checking if already node present or not.
            self.head = Node(data)  # Creating a node if list is empty.
            self.last = self.head
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def print_list(self):
        temp = self.head  # assigning head to temporary variable temp
        while temp is not None:  # traversing through list till it ends.
            print(temp.data, end=' ')
            temp = temp.next

    def search(self, dt):
        if self.head.data == dt:  # if data found in very 1st node i,e head
            self.head = self.head.next  # assign head to next node. (i,e deleted 1st node)
        else:
            temp = self.head
            prev = None
            while temp is not None:  # Traversing through list.
                if temp.data == dt:  # if data found in current temp node then
                    prev.next = temp.next  # assign previous nodes next to current node next
                # i,e deleting current temp node.
                    return
                else:
                    prev = temp
                    temp = temp.next
            if temp is None:
                self.insert(dt)

    def pop(self):
        var = []
        while self.head is not None:
            var.append(self.head.data)
            self.head = self.head.next
        return var

    def first(self):
        var = []
        while self.head is not None:
            var.append(self.head.data)  # adding each of the nodes data ie words into list var
            self.head = self.head.next
        return var

#  ***************************************  STACK  ***********************************************


class Stack:
    def __init__(self):
        self.head = None
        # self.last = None

    def push(self, data):
        if self.head is None:  # Checking if already node present or not.
            self.head = Node(data)  # Creating a node if list is empty.
            # self.last = self.head
        else:
            temp = Node(data)  # Adding node before last node.
            temp.next = self.head
            self.head = temp

    def pop(self):
        if self.head is not None:  # If stack is not empty
            var = self.head.data  # obtaining top element in var
            self.head = self.head.next  # moving head to next element
            return var  # returning head element.
        else:
            print("Can't Pop item...List is Empty")

    def peek(self):
        if self.head is not None:
            item = self.head.data  # Returning Top of the stack.
            return item
        else:
            print("Can't peek item...List is Empty")

    def is_empty(self):
        if self.head is None:  # If head is found to be None it returns true
            return True
        else:
            return False

    def size(self):
        cnt = 0
        temp = self.head
        while temp is not None:
            cnt += 1  # Incrementing cnt for each None
            temp = temp.next
        return cnt  # returning cnt i,e size of List

#  *****************************  Queue for Banking  *************************************


class Queue:
    def __init__(self, lent):
        self.lent = lent
        self.front = None
        self.rear = None
        self.balance = 1000
        self.size = 0

    def enqueue(self, amt):
        if self.lent == self.size:
            print("Queue is Full.")
        else:
            if self.front is None:
                self.front = Node(amt)
                self.rear = self.front
                self.size += 1
                self.balance = self.balance + amt
                print("amount Deposited.")
            else:
                self.rear = Node()

