# *********************************************************************************************
# Purpose: To write a program to Palindrome using Queue- Linked List.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
from Utility import LinkedList


def main():
    str = input("Enter a string to check Palindrome")
    str2 = list(str)  # Converting string into List
    ll = LinkedList()
    for i in str2:
        ll.insert_rev(i)
    str3 = ll.pop()
    str2 = ''.join(str3)
    if str == str2:
        print("String", str, "is palindrome")
    else:
        print("String", str, "is Not a palindrome")


if __name__ == "__main__":
    main()
