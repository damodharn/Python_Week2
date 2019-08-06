class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, lent):
        self.lent = lent
        self.front = None
        self.rear = None
        self.balance = 1000
        self.size = 0

    # Method to add money into Bank Account. i,e Deposit process
    def enqueue(self, choice):
        if self.lent == self.size:  # If Queue is Full print message and don't add any further node.
            print("Queue is Full.")
        else:
            if self.front is None and choice == 1:
                amt = int(input("Enter an amount to be Deposited."))
                self.front = Node(amt)
                self.rear = self.front
                self.size += 1
                self.balance = self.balance + amt
                print(amt, "Rs. Amount Deposited.")
            elif self.front is None and choice == 2:
                amt = int(input("Enter an amount you wanted to Withdraw."))
                self.front = Node(amt)
                self.rear = self.front
                self.size += 1
                if self.balance >= amt:
                    self.balance = self.balance - amt
                    print(amt, "Rs. Amount debited...")
                else:
                    print("Not sufficient amount is available.")
            else:
                if choice == 1:
                    amt = int(input("Enter an amount you wanted to Deposit."))
                    temp = Node(amt)
                    self.rear.next = temp
                    self.rear = temp
                    self.balance += amt
                    print(amt, "Rs. Amount Deposited.")
                elif choice == 2:
                    amt = int(input("Enter an amount you wanted to Deposit."))
                    temp = Node(amt)
                    self.rear.next = temp
                    self.rear = temp
                    if self.balance >= amt:
                        self.balance += amt
                        print(amt, "Rs. Amount Deposited.")
                    else:
                        print("No sufficient amount is available.")
    # Method to Withdraw money from bank account.

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty.")
        else:
            self.front = self.front.next


    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False