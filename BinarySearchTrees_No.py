# *********************************************************************************************
# Purpose: To write a program to Find No of possible BSTs for given Nos.
# Author:  Damodhar D. Nirgude.
# **********************************************************************************************


class BST:
    @staticmethod
    def bst(no):  # Finding Possible BST trees No using Recursive Method.
        if no <= 1:
            return 1
        res = 0
        for i in range(no):
            res += BST.bst(i) * BST.bst(no - i - 1)
        return res


def main():
    in_arr = []
    out_arr = []
    try:
        no = int(input("Enter a Count of No.s U wanted to Know possibilities of BST's."))
        for i in range(no):
            print("Enter", i+1, 'Value')
            in_arr.append(int(input()))
    except Exception as e:
        print("Invalid i/p...Enter only Integer values\n", e, "\nTerminating Program...")
    for i in in_arr:
        val = BST.bst(i)
        out_arr.append(val)
    print("Input:", in_arr)
    print("Output:", out_arr)


if __name__ == '__main__':
    main()