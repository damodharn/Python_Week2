# *********************************************************************************************
# Purpose: To write a program to Find prime Anagram nos upto range 1000 and storing them in 2D array in proper range.
# Author:  Damodhar D. Nirgude.
# **********************************************************************************************
from Prime_2D import Prime


class Anagram:

    def anagram(self, arr):
        ar = []
        for i in arr:
            if i > 10:
                sum1 = 0
                no = i
                while no != 0:
                    temp = no % 10
                    sum1 = (sum1 * 10) + temp
                    no = no // 10
                if sum1 in arr:
                    ar.append(i)
        return ar


def main():
    lis = [[], []]
    arr = Prime().primeno()
    arr1 = Anagram().anagram(arr)
    for i in arr:
        if i in arr1:
            lis[0].append(i)
        else:
            lis[1].append(i)
    print("List:______________________________________________________________________________________")
    for i in range(2):
        if i == 0:
            print("Anagram List:", end=" ")
        else:
            print("Not anagram List:", end=" ")
        print(lis[i])
        print(len(lis[i]))


if __name__ == "__main__":
    main()