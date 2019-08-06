# *********************************************************************************************
# Purpose: To write a program to store Week day in Queue for a given Calendar month.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
from Calander_2D import Calendar
import numpy


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def en_queue(self, data):    # Method to enqueue object in the Queue.
        if self.front is None:
            self.front = Node(data)
            self.rear = self.front
        else:
            temp = Node(data)
            self.rear.next = temp
            self.rear = temp
        self.size += 1

    def de_queue(self):   # Method to De-Queue Object from queue.
        if self.front is None:
            print("Queue is Empty.")
        else:
            item = self.front.data
            self.front = self.front.next
            self.size -= 1
            return item

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def q_size(self):
        return self.size


def main():
    cl = Calendar()
    qq = Queue()
    try:
        while True:  # into the loop till user enter valid month
            month = int(input("Enter a Month"))
            if (month >= 1) and (month <= 12):
                break
            else:
                print("Enter month between 1 to 12")
                continue
        while True:  # into the loop till user enter year in the range of 1000 to 9999
            year = int(input("Enter a Year"))
            if (year > 999) and (year <= 9999):
                break
            else:
                print("Enter year in range 2000 to 9999")
                continue
    except ValueError as e:
        print(e)
    else:
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        weekday = ['Sun', 'Mon', 'Tue', 'Wed', 'Fri', 'Thr', 'Sat']
        ll = Calendar()
        if ll.leap_year(year) is True:  # If user entered year is leap year
            days[2] = 29  # then updating days of FEB month to 29 days
        empty = ll.days(1, month, year)  # Give us the day of 1st day of the month, So we can left days before it empty.
        array = numpy.zeros((6, 7), dtype=int)
        x = 1  # x will give us the date.
        for i in range(6):
            for j in range(7):
                if x == 1 and (j == empty):  # adding 1st day at proper position in an 2D-Array.
                    array[i][j] = x
                    x += 1
                elif (x != 1) and (x <= days[month]):
                    array[i][j] = x
                    x += 1
                else:
                    array[i][j] = 0
        print(array)
        # for i in range(len(weekday)):
        #     weekday[i] = Queue()
        #     weekday[i].en_queue(array[][])

if __name__ == '__main__':
    main()