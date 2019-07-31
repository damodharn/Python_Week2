# *********************************************************************************************
# Purpose: To write a program to print Calendar for a current month.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
import numpy

# **********************************  Calendar  *****************************************


class Calendar:

    #  **********************  Method returns day value i,e 1st day of the month  *****************

    def days(self, d, m, y):
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7
        return d0

    def leap_year(self, yr):
        if yr % 100 == 0:  # Checking Conditions for leap year
            if yr % 400 == 0:  # and returning 1 if Leap year is found and 0 if not found.
                return True
            else:
                return False
        elif yr % 4 == 0:
            return True
        else:
            return False


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
    empty = ll.days(1, month, year)  # Give us the day of 1st day of the month
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
    print("_____________________________")
    print("       CALENDAR     ", month, year, "|")
    print("-----------------------------")
    print("                  ", months[month], year, "|")
    print("_____________________________")
    print("Sun Mon Tue Wed Thr Fri Sat |")
    print("_____________________________")
    for i in range(6):
        for j in range(7):
            z = array[i][j]
            if z == 0:
                print(end="    ")
            else:
                if z // 10 == 0:
                    print(array[i][j], end="   ")
                else:
                    print(z, end="  ")
                if j == 6:
                    print("|")


if __name__ == '__main__':
    main()
