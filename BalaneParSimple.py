# *********************************************************************************************
# Purpose: To write a program to check if Expression is balanced or not using Stack.
# Author: Damodhar D. Nirgude.
# *********************************************************************************************

#  ***************************************  STACK  ***********************************************


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 10

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        var = self.stack.pop()
        return var

    def is_full(self):
        if len(self.stack) == self.size:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.stack) < 1:
            return True
        else:
            return False

#  Method to check Expression  **************************


def balance(exp):
    ps = 0  # store count for Push operation
    pp = 0  # Store count for Pop operation.
    flag = True
    ss = Stack()
    for i in exp:  # Traversing in an Expression.
        if i == '(':
            if ss.is_full() is False:  # If stack is not full then push '(' into stack.
                ss.push(i)
                ps += 1
            else:   # If stack found to be full then set full to some value and return it.
                full = 404
                print("Stack if Full")
                return full
        elif i == ')':  # If ')' is found in an Expression.
            if ss.is_empty() is False:  # and If Stack is not Empty then pop item from it.
                ss.pop()
                pp += 1
            else:  # If stack is empty and ')' is found then set flag as False and break the loop.
                flag = False
                break
    if ps == pp and flag is True:  # If count of Push and Pop is equal and if flag is True ,return True
        return True
    else:
        return False

#  *****************************  Main Method  *********************


def main():
    exp = input("Enter ur exp")  # Taking input from User.
    res = balance(exp)  # Passing Expression to Method to check if it is balanced or not.
    if res != 404:  # If Stack is not full then this block will get executed.
        if res is True:
            print("Balanced")
        else:
            print("Not balanced")
    else:  # If stack was full due to lot of continuous opening braces, print message
        print("Stack was full, so couldn't check")


if __name__ == '__main__':
    main()