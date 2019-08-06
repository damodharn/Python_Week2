# *********************************************************************************************
# Purpose: To write a program to create Ordered Linked list of Numbers to add/delete user's No. into/from file.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#  *********************************  ORDERED LIST  *********************************************


class LinkList2:
    def __init__(self):
        self.head = None

    # Method to insert a Node at Particular place in the List.

    def insert_at(self, data):
        if self.head is None:  # If List is found to be Empty
            self.head = Node(data)  # then create a new node and assign head to it.
        else:
            if self.head.data > data:  # If data is found to be greater than head i,e 1st node data
                temp = Node(data)  # then insert new node before 1st node i,e head node and update head to new node.
                temp.next = self.head
                self.head = temp
            else:
                prev = None
                temp = self.head
                while temp is not None:  # Traverse in the list either till last or
                    if temp.data > data:  # till we get current node data greater than new data
                        prev.next = Node(data)  # and insert new node before current node.
                        prev.next.next = temp
                        break
                    prev = temp
                    temp = temp.next
                if temp is None:  # If new data is largest no
                    temp = Node(data)  # then add it at the last of the list.
                    prev.next = temp

    def print_list(self):
        temp = self.head  # assigning head to temporary variable temp
        while temp is not None:  # traversing through list till it ends.
            print(temp.data, end=' ')
            temp = temp.next

    # Method to fetch 1st node data from the list.

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
            elif temp.data > no:  # If Number not found till last or if we got No greater than i/p no
                #  Inserting the New Node at that place
                prev.next = Node(no)
                prev.next.next = temp


def main():
    words = []
    try:
        fo = open("OrderedNo.txt", "r")  # Opening txt file in Read mode to read it's data.
    except FileNotFoundError as e:
        print(e)
    else:
        arr = fo.read()  # reading files data into arr as a string.
        words = arr.split()  # splitting string of words and then adding each word into list words
        # print(type(words))
        fo.close()
        print("Words: ", words, "\n")
        arr1 = []
        try:
            for i in words:
                arr1.append(int(i))  # adding each no. into array arr1.
        except ValueError as e:
            print(e)
        else:
            print("arr1:", arr1)
            ll = LinkList2()
            for i in range(len(arr1)):
                data = int(arr1[i])
                ll.insert_at(data)  # Inserting each no in Link list in Ascending order.
            print('Ordered list: ', end=' ')
            ll.print_list()
            try:
                no = int(input("\nEnter a No. to Insert or pop from list"))  # Taking i/p from User
            except ValueError as e:
                print(e)
            else:
                ll.search(int(no))
                ll.print_list()
                fo = open("OrderedNo.txt", "w")
                arr2 = ll.pop()  # Taking Ordered No.s from Link list in array arr2
                for i in arr2:  # Writing each element into the file.
                    fo.write(str(i) + " ")
                fo.close()


if __name__ == "__main__":
    main()