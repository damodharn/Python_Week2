# *********************************************************************************************
# Purpose: To write a program to create Queue for Banking.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************


class Queue:

    def __init__(self, lent):
        self.queue = lent*[]
        self.size = 0
        self.lent = lent
        self.balance = 2000
        self.i = 0

    #  Method enque() insert each person in the queue.

    def enque(self, ch):
        self.size += 1
        self.queue.insert(0, ch)

    def is_full(self):
        if self.lent == self.size:
            return True
        else:
            return False

    #  Method to de-queue people from Queue after completing their banking work.

    def deque(self):
        self.i += 1
        action = self.queue.pop()  # Fetching action (i,e what need to be done) from queue.
        if action == 1:  # If action is 1 then Deposit money into bank.
            print("Person", self.i, "Enter an Amount you wanted to be Deposited:", end=' ')
            amt = int(input())
            self.balance += amt
            self.size -= 1
            print(amt, "Rs. Deposited")
            print("Available Balance in Bank:", self.balance)
        elif action == 2:  # If action is 2 then Withdraw money from Bank if available.
            print("Person", self.i, "Enter an amount you wanted to Withdraw", end=' ')
            amt = int(input())
            if amt <= self.balance:
                self.balance -= amt
                self.size -= 1
                print(amt, "Rs. Debited.")
                print("Available Balance in Bank:", self.balance)
            else:
                print("No sufficient Cash is available")

    # Method to give if Queue is empty or not.

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


def main():
    size = 5
    i = 0
    qq = Queue(size)
    while True:
        print("Person", i+1, "Enter ur choice:")
        print("1: To Deposit\n2: To Withdraw\n3: Exit")  # Printing i/p Menu providing choices for User.
        choice = int(input())
        if choice == 1 or choice == 2:  # If choice is either 1 or 2 then add people into queue.
            if qq.is_full() is True:  # Print message if queue is full and then exit from loop.
                print("Queue is full\n")
                break
            else:
                i += 1
                qq.enque(choice)
        elif choice == 3 or qq.is_full() is True:  # ask to enter choice 3 if people are less than max queue size.
            break
        else:
            print("wrong choice")
    print(i, "Persons are there in Queue.\n")
    while True:  # After adding people into queue
        if qq.is_empty() is True:
            print("\nQueue is Empty")
            break
        else:
            qq.deque()  # De-queue each person from queue after work is done till queue finishes.


if __name__ == '__main__':
    main()