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
        elif self.head.data > new.data:
            new.next = self.head
            self.head = new
        else:
            prev = None
            temp = self.head
            while temp is not None:
                if temp.data > new.data:
                    new.next = temp
                    prev.next = new
                    break
                prev = temp
                temp = temp.next
            # prev.next = new
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