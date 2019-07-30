import numpy

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
                arr.append(x)
        return arr


def main():
    ll = Prime()
    arr = ll.primeno()
    array = numpy.zeros((10, 168), dtype=int)
    for j in range(len(arr)):
        if arr[j] <= 100:
            array[0][j] = arr[j]
        elif (arr[j] > 100) and (arr[j] <= 200):
            array[1][j] = arr[j]
        elif (arr[j] > 200) and (arr[j] <= 300):
            array[2][j] = arr[j]
        elif (arr[j] > 300) and (arr[j] <= 400):
            array[3][j] = arr[j]
        elif (arr[j] > 400) and (arr[j] <= 500):
            array[4][j] = arr[j]
        elif (arr[j] > 500) and (arr[j] <= 600):
            array[5][j] = arr[j]
        elif (arr[j] > 600) and (arr[j] <= 700):
            array[6][j] = arr[j]
        elif (arr[j] > 700) and (arr[j] <= 800):
            array[7][j] = arr[j]
        elif (arr[j] > 800) and (arr[j] <= 900):
            array[8][j] = arr[j]
        else:
            array[9][j] = arr[j]
    print(arr)
    #  ***********************************  Printing Array elements  ***********************************


if __name__ == '__main__':
    main()