# *********************************************************************************************
# Purpose: To write a program to check if Expression is balanced or not using stack.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
from Utility import Stack


def main():
    psh = 0
    pp = 0
    exp = input("Write ur Expression")
    flag = True
    ll = Stack()
    for i in exp:
        if i == '(':
            ll.push(i)
            psh += 1
        elif i == ')':
            if ll.is_empty() is True:
                flag = False
                break
            else:
                j = ll.pop()
                pp += 1
    if flag is True and psh == pp:
        print("Balanced Eqn")
    else:
        print("Unbalanced Eqn")


if __name__ == "__main__":
    main()