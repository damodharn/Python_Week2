# *********************************************************************************************
# Purpose: To write a program to create Unordered Linked list of words to add/delete user's word into/from file.
# Author:  Damodhar D. Nirgude.
# ************************************************************************************************


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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
                prev = temp
                temp = temp.next
            if temp is None:
                temp = Node(dt)
                prev.next = temp

    def pop(self):
        var = []
        while self.head is not None:
            var.append(self.head.data)
            self.head = self.head.next
        return var


def main():
    fo = open("Unordered.txt", "r")  # Opening txt file in Read mode to read it's data.
    arr = fo.read()  # reading files data into arr as a string.
    words = arr.split(" ")  # splitting string of words and then adding each word into list words
    fo.close()
    ll = LinkedList()  # Creating object ll of LinkedList
    for i in words:
        ll.insert(i)  # inserting each word into the list.
    ll.print_list()
    data = input("\n\nEnter a word to be searched in the list to add/delete: ")  # Taking i/p from user.
    ll.search(data)  # Searching the user entered data into the list and then adding/deleting
    # it into/from the list.
    ll.print_list()
    array1 = ll.pop()
    fo = open("Unordered.txt", "w")  # Opening txt file in Write mode.
    for i in array1:
        fo.write(i + " ")  # writing each word int the file.
    fo.close()


if __name__ == "__main__":
    main()