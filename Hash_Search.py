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
        if self.head is None:  # If head is None i,e List is Empty
            self.head = new  # So assign newly created node to Head
        elif new.data > self.head.data:  # if New data found to be greater than head data
            new.next = self.head   # then insert it before head
            self.head = new  # and Update head
        else:
            prev = None
            temp = self.head
            while temp is not None:  # Traverse in the list either till list ends or till data found
                if new.data > temp.data:  # if data found to be greater then temp node's data
                    new.next = temp  # then insert that node before temp
                    prev.next = new
                    break
                prev = temp
                temp = temp.next
            if temp is None:  # If data not found to be greater than temp node data till last of the list
                prev.next = new  # then Add that new node at the Last of the List.

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
        if self.head.data == data:  # If data found at head then move head to next node
            self.head = self.head.next
        else:
            temp = self.head
            prev = None
            while temp is not None:  # Traverse in the list till data not found
                if temp.data == data:  # and delete the node where data found.
                    prev.next = temp.next
                prev = temp
                temp = temp.next

    #  *******************************  Method to display List elements  *****************************

    def display(self):
        if self.head is None:
            pass
        else:
            temp = self.head
            while temp is not None:  # Print each node's data till last node
                print(temp.data, end=" ")
                temp = temp.next

    # Function returns size of Link list for each slot

    def slot_size(self):
        size = 0
        temp = self.head
        while temp is not None:
            size += 1  # Increase the size count for each Node till last node found
            temp = temp.next
        return size
    #  ************************************  Method gives us Head value and update head   *********************

    def pop_head(self):
        if self.head is not None:
            data = self.head.data  # Get data from head node and update head to next node
            self.head = self.head.next
            return data
        return

#  ***************************************  Main Method  **************************************************


def main():
    fo = open("HashText.txt", "r")
    arr = fo.read()
    print(arr)
    words = arr.split(' ')
    fo.close()
    print(words)
    slot = []
    for i in range(11):  # Fill each slot with object of class Hash
        hs = Hash()
        slot.append(hs)
    for i in range(len(words)):
        slot[int(words[i]) % 11].insert(int(words[i]))  # Inserting each No. at proper slot with proper index.

    for i in range(len(slot)):  # Loop to display list from each slot.
        print(i + 1, "}", end=" ")
        print(slot[i].display())

    no = int(input("Enter a No. to be Searched in List"))
    index = no % 11  # Dividing No by 11 to get proper Index position in slot.
    flg = slot[index].search(no)  # Searching user entered No at particular index slot
    if flg is True:
        print("\nNo", no, "found and Deleted from list\n")
        slot[index].delete(no)  # If No found then Deleting the no
    else:
        print("\nNo", no, "not found and added to the list\n")
        slot[index].insert(no)  # If No not found in the list then inserting the no into the list.
    for i in range(len(slot)):
        print(i + 1, "}", end=" ")  # for i in slot:
        print(slot[i].display())

    fo = open("HashText.txt", "w")  # Opening file in Write mode to write nos from list into it
    for i in range(11):
        if slot[i] is not None:
            size = slot[i].slot_size()
            for j in range(size):
                fo.write(str(slot[i].pop_head())+' ')
        else:
            pass
    fo.close()


if __name__ == "__main__":
    main()