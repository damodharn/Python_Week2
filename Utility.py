class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList2:
    def __init__(self):
        self.head = None

    def insert_at(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            if self.head.data > data:
                temp = Node(data)
                temp.next = self.head
                self.head = temp
            else:
                prev = None
                temp = self.head
                while temp is not None:
                    if temp.data > data:
                        prev.next = Node(data)
                        prev.next.next = temp
                        break
                    prev = temp
                    temp = temp.next
                if temp is None:
                    temp = Node(data)
                    prev.next = temp

    def print_list(self):
        temp = self.head  # assigning head to temporary variable temp
        while temp is not None:  # traversing through list till it ends.
            print(temp.data, end=' ')
            temp = temp.next

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
                temp.next = None
            elif temp.data > no:  # If No not found till last or if we got No greater than i/p no
                #  Inserting the New Node at that place
                prev.next = Node(no)
                prev.next.next = temp


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
                else:
                    prev = temp
                    temp = temp.next
            if temp is None:
                self.insert(dt)

    def first(self):
        var = []
        while self.head is not None:
            var.append(self.head.data)  # adding each of the nodes data ie words into list var
            self.head = self.head.next
        return var
