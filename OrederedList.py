# *********************************************************************************************
# Purpose: To write a program to create Ordered Linked list of Numbers to add/delete user's No. into/from file.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
from Utility import LinkList2


def main():
    fo = open("OrderedNo.txt", "r")  # Opening txt file in Read mode to read it's data.
    arr = fo.read()  # reading files data into arr as a string.
    words = arr.split()  # splitting string of words and then adding each word into list words
    # print(type(words))
    fo.close()
    print("Words: ", words, "\n")
    arr1 = []
    for i in words:
        arr1.append(int(i))  # adding each no. into array arr1.
    print("arr1:", arr1)
    ll = LinkList2()
    for i in range(len(arr1)):
        data = int(arr1[i])
        ll.insert_at(data)  # Inserting each no in Link list in Ascending order.
    print('list: ', end=' ')
    ll.print_list()
    no = int(input("\nEnter a No. to Insert or pop from list"))  # Taking i/p from User
    ll.search(int(no))
    ll.print_list()
    fo = open("OrderedNo.txt", "w")
    arr2 = ll.pop()  # Taking Ordered No.s from Link list in array arr2
    for i in arr2:  # Writing each element into the file.
        fo.write(str(i) + " ")
    fo.close()


if __name__ == "__main__":
    main()