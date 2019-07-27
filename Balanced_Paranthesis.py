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
            # print("'(' is Pushed into the stack")
            psh += 1
        elif i == ')':
            if ll.is_empty() is True:
                flag = False
                # print("Can't Pop...List is empty")
                break
            else:
                j = ll.pop()
                # print(j, "is Popped from the stack")
                pp += 1
    if flag is True and psh == pp:
        print("Balanced Eqn")
    else:
        print("Unbalanced Eqn")


if __name__ == "__main__":
    main()