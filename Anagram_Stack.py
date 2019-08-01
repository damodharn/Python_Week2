# ************************************************************************************************
# Purpose: To write a program to Find prime Anagram nos up to range 1000 and storing them in stack using Link List.
# Author:  Damodhar D. Nirgude.
# ************************************************************************************************
import time

# ###########################  Class Prime_Anagram to give Prime Anagram Nos  #####################


class Prime_Anagram:
    def primeno(self):
        arr = []
        for x in range(2, 1000):  #
            prime = 1
            for y in range(2, (x // 2) + 1):  # dividing no x by each no which are less than or equal to it's half.
                if x % y == 0:
                    prime = 0
                    break
            if prime == 1:
                arr.append(x)  # Storing prime no into array arr
        return arr

    def anagram(self, arr):
        ar = []
        for i in arr:
            if i > 10:
                sum1 = 0
                no = i
                while no != 0:
                    temp = no % 10
                    sum1 = (sum1 * 10) + temp
                    no = no // 10
                if sum1 in arr:
                    ar.append(i)
        return ar


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ####################################### Stack Using Link List  ############################################
class Stack:
    def __init__(self):
        self.top = None
        self.size = 100
        self.cnt = 0

    # *******************************  Method insert element at the Top  *****************************

    def push(self, data):
        if self.top is None:  # Check if stack is Empty and if found empty
            self.top = Node(data)  # Add element at the Top
            self.cnt += 1
        else:  # Else add the element before Top and Update top to Newly added element.
            temp = Node(data)
            temp.next = self.top
            self.top = temp
            self.cnt += 1

    # ***************************  Method give top element and remove it. *********************

    def pop(self):
        val = self.top.data
        self.top = self.top.next
        self.cnt -= 1
        return val

    # **********************************  Method checks if Stack is Empty or not  ***********************

    def is_empty(self):
        if self.top is None:
            return True  # Returns True if Found Empty.
        else:
            return False  # Return False if not found empty.
    # ********************************  Method to check if stack become Full or not  ************************

    def is_full(self):
        if self.cnt == self.size:
            return True
        else:
            return False

    def stack_size(self):
        return self.cnt

    def peek(self):
        return self.top.data  # Return Top element

# ###########################################  MAIN Method #################################################


def main():
    ss = Stack()
    pa = Prime_Anagram()
    ar = pa.anagram(pa.primeno())
    start_time = time.time()
    print("Pushing data into the Stack...")
    while (time.time() - start_time) < 1:
        continue
    for i in ar:
        if ss.is_full() is False:
            ss.push(i)
        else:
            print("Stack is Full...Can't PUSH item")
            break
    print("\nData Pushed into the Stack\n\nSize of a Stack: ", ss.stack_size())
    start_time = time.time()
    while (time.time() - start_time) < 1:
        continue
    print("\nPrinting Anagram No in Reverse Order:...")
    start_time = time.time()
    while (time.time() - start_time) < 1:
        continue
    while True:
        if ss.is_empty() is False:
            print(ss.pop(), end=" ")
        else:
            print("\nStack is Empty ")
            break
    print("\nSize of Stack after Popping data from Stack: ", ss.stack_size())


if __name__ == "__main__":
    main()