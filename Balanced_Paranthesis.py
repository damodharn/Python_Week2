# *********************************************************************************************
# Purpose: To write a program to check if Expression is balanced or not using stack.
# Author: Damodhar D. Nirgude.
# *********************************************************************************************

#  Class Node : Each node object contain each data element in Stack.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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


def main():
    psh = 0
    pp = 0
    exp = input("Write ur Expression")
    flag = True
    ll = Stack()
    for i in exp:
        if i == '(':  # If open parenthesis found in expression then push it to stack.
            ll.push(i)
            psh += 1
        elif i == ')':
            if ll.is_empty() is True:
                flag = False
                break
            else:
                j = ll.pop()  # If closed parenthesis found in expression then pop the stack.
                pp += 1
    if flag is True and psh == pp:  # If push and pop count found to be equal then
        print("Balanced Eqn")  # eqn is Balanced else eqn is Unbalanced.
    else:
        print("Unbalanced Eqn")


if __name__ == "__main__":
    main()