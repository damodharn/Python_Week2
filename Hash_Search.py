# *********************************************************************************************
# Purpose: To write a program to create Queue for Banking.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
# from Utility import Hash


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#  *********************************  Hashing Search  *************************************


class Hash:
    def __init__(self):
        self.head = None

    #  ***********************************  Method to Insert Element at Ordered place  ****************

    def insert(self, data):
        new = Node(data)   # Assigning newly created node to new
        if self.head is None:
            self.head = new
        elif new.data > self.head.data:
            new.next = self.head
            self.head = new
        else:
            prev = None
            temp = self.head
            while temp is not None:
                if new.data > temp.data:
                    new.next = temp
                    prev.next = new
                    break
                prev = temp
                temp = temp.next
            if temp is None:
                prev.next = new
    #  *************************************  Method to search element in List  **************************

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    #  *******************************  Method to delete Element from the List  ****************

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

    #  *******************************  Method to display List elements  *****************************

    def display(self):
        if self.head is None:
            pass
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
    slot = []
    for i in range(lent):
        hs = Hash()
        slot.append(hs)
    for i in range(lent):
        slot[int(words[i]) % 10].insert(int(words[i]))
    for i in range(lent):
        print(i + 1, "}", end=" ")  # for i in slot:
        print(slot[i].display())        # print(i.display())
    no = int(input("Enter a No. to be Searched in List"))
    for i in range(lent):
        if slot[i].search(no) is True:
            break
    
    for i in range(lent):
        print(slot[i].display())


if __name__ == "__main__":
    main()