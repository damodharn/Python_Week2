# *********************************************************************************************
# Purpose: To write a program to Find prime nos upto range 1000 and storing them in 2D array in proper range.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************


class Prime:

    def primeno(self):
        arr = []
        for x in range(2, 1000):  #
            prime = 1
            for y in range(2, (x // 2) + 1):  # dividing no x by each no which are less than or equal to it's half.
                if x % y == 0:
                    prime = 0
                    break
            if prime == 1:
                arr.append(x)  # Storing prime no into array arr
        return arr


def main():
    ll = Prime()
    arr = ll.primeno()
    array = [list() for i in range(10)]  # Created 2D array of 10 rows; each row for each range like 0 to 100 and so on
    for i in range(0, 10):
        c = 0
        for j in range(i*100, (i+1)*100):
            if j in arr:
                array[i].append(j)  # Added each No in it's appropriate range.
                c += 1
    #  ***********************************  Printing Array elements  ***********************************
    print("\nRange     |  <----------------------- List ------------------------>")
    print("____________________________________________________________________________________________________")
    for i in range(10):
        print(i*100, "to", (i+1)*100, "| ", array[i])
        print("________________________________________________________________________________________________")


if __name__ == '__main__':
    main()