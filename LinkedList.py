# *********************************************************************************************
# Purpose: To write a program to create Unordered Linked list of words to add/delete user's word into/from file.
# Author:  Damodhar D. Nirgude.
# ************************************************************************************************
from Utility import LinkedList


def main():
    fo = open("Unordered.txt", "r")  # Opening txt file in Read mode to read it's data.
    arr = fo.read()  # reading files data into arr as a string.
    # print(type(arr))
    print("Array: ", arr)
    words = arr.split(" ")  # splitting string of words and then adding each word into list words
    # print(type(words))
    fo.close()
    print("Words", words, "\n")
    ll = LinkedList()  # Creating object ll of LinkedList
    for i in words:
        ll.insert(i)  # inserting each word into the list.
    ll.print_list()
    data = input("\n\nEnter a word to be searched in the list to add/delete: ")  # Taking i/p from user.
    ll.search(data)  # Searching the user entered data into the list and then adding/deleting
    # it into/from the list.
    ll.print_list()
    array1 = ll.first()
    # print("\n", type(array1))
    fo = open("Unordered.txt", "w")  # Opening txt file in Write mode.
    for i in array1:
        fo.write(i + " ")  # writing each word int the file.
    fo.close()


if __name__ == "__main__":
    main()