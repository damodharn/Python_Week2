# *********************************************************************************************
# Purpose: To write a program to create Queue for Banking.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
# from Utility import Hash


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Hash:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new  # If list is empty assigning head with new
        elif self.head.data > new.data:  # If 1st element is bigger than new element
            new.next = self.head  # Link head with new
            self.head = new  # update head with new.
        else:  # Else traverse in the list till proper place and insert element there.
            prev = None
            temp = self.head
            while temp is not None:
                if new.data > temp.data:  # if new node data is greater than temp data
                    new.next = temp  # insert new node before temp
                    prev.next = new
                    break
                prev = temp
                temp = temp.next
            if temp is None:
                prev.next = new
    #  *******************************  Search Element in List and
    #  return True if found anf False if not Found  *************************************

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False
    #  ********************  Method to delete node if data found in the List  ******************

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            prev = None
            while temp is not None:
                if temp.data == data:
                    prev.next = temp.next
                prev = temp
                temp = temp.next
    #  **************************************  Method display List elements  ********************

    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next


def main():
    fo = open("HashText.txt", "r")
    arr = fo.read()
    print(arr)
    words = arr.split(' ')
    fo.close()
    print(words)
    lent = len(words)
    ll_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ll = Hash()
    for i in range(len(ll_arr)):
        ll = Hash()
        ll_arr.append(len(ll_arr))
    for i in range(lent + 1):
        ll_arr[words[i] % 11].insert((words[i]))
    for i in range(len(ll_arr)):
        print(ll_arr[i].display())


if __name__ == "__main__":
    main()