# *********************************************************************************************
# Purpose: To write a program to print Calendar for a current month.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
import numpy
from Utility import Calendar


def main():
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
    except Exception as e:
        print(e)
        return
    months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ll = Calendar()
    if ll.leap_year(year) is True:  # If user entered year is leap year
        days[2] = 29  # then updating days of FEB month to 29 days
    print(days)
    empty = ll.days(1, month, year)  # Give us the day of 1st day of the month
    print(empty)
    array = numpy.zeros((6, 7), dtype=int)
    x = 1  # x will give us the date.
    for i in range(6):
        for j in range(7):
            if x == 1 and (j == empty):
                array[i][j] = x
                x += 1
            elif (x != 1) and (x <= days[month]):
                array[i][j] = x
                x += 1
            else:
                array[i][j] = 0
    print(array)
    print(" CALENDAR ", month, " ", year)
    print("---------------------------------")
    print("", months[month], "  ", year)
    print("---------------------------------")
    # print("S M T W Th F Sa ")
    print("---------------------------------")

    for i in range(5):
        for j in range(7):
            if array[i][j] != 0:
                z = array[i][j]
                if z//10 == 0:
                    print(z, end="  ")
                else:
                    print(z, end=" ")
            else:
                print(end="  ")
        print()


if __name__ == '__main__':
    main()
