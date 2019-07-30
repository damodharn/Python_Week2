import numpy


def prime_Numbers(start):
    """generating prime numbers"""
    counter = 0
    arr = []
    for i in range(0, start):
        count = 0
        if i != 0 and i != 1:
            for j in range(2, i):
                if i % j == 0:
                    count = count + 1
                    break
            if count == 0:
                arr.append(i)
    array = numpy.zeros((10, 168))
    """Printing prime number between 0 to 100"""
    for i in range(0, 100):
        if arr[i] < 100:
            array[0][i] = arr[i]
    for i in array[0]:
        if i == 0 and i < 100:
            continue
        print(int(i), end=" ")
    print("\n")

    """Printing prime number between 100 to 200"""
    for i in range(0, len(arr)):
        if arr[i] > 100 and arr[i] < 200:
            array[1][i] = arr[i]
    for i in array[1]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 200 to 300"""
    for i in range(0, len(arr)):
        if arr[i] > 200 and arr[i] < 300:
            array[2][i] = arr[i]
    for i in array[2]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 300 to 400"""
    for i in range(0, len(arr)):
        if arr[i] > 300 and arr[i] < 400:
            array[3][i] = arr[i]
    for i in array[3]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 400 to 500"""
    for i in range(0, len(arr)):
        if arr[i] > 400 and arr[i] < 500:
            array[4][i] = arr[i]
    for i in array[4]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 500 to 600"""
    for i in range(0, len(arr)):
        if arr[i] > 500 and arr[i] < 600:
            array[5][i] = arr[i]
    for i in array[5]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 600 to 700"""
    for i in range(0, len(arr)):
        if arr[i] > 600 and arr[i] < 700:
            array[6][i] = arr[i]
    for i in array[6]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 700 to 800"""
    for i in range(0, len(arr)):
        if arr[i] > 700 and arr[i] < 800:
            array[7][i] = arr[i]
    for i in array[7]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 800 to 900"""
    for i in range(0, len(arr)):
        if arr[i] > 800 and arr[i] < 900:
            array[8][i] = arr[i]
    for i in array[8]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")
    """Printing prime number between 900 to 1000"""
    for i in range(0, len(arr)):
        if arr[i] > 900 and arr[i] < 1000:
            array[9][i] = arr[i]
    for i in array[9]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    print(array)

    """ Main Method"""


if __name__ == '__main__':
    """
    start of main method
    validation of the range
    Calling the prime_Numbers Method 
    with start as Method Argument

    """
    print()
    print("========================0 to 1000 prime numbers=========================")
    print()

    start = int(input("Enter Range: "))
    if start == 1000:
        prime_Numbers(start)
    else:
        print("Range should be 1000")
