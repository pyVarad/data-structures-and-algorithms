"""Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic
An array is said to be monotonic if its element, from left to right are entirely non-increasing or non-decreasing.
Non-increasing elements aren't necessarily exclusively decreasing, they simply don't increase. Similarly non-decreasing
are not exclusively increasing, they simply mean they don't decrease.

Note that empty arrays or array's with one element are also monotonic.

Sample Input
------------
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output
-------------
true
"""


def is_monotonic(array):
    if len(array) > 1:
        ptr_1 = 0
        ptr_2 = 1
        trend = ""

        while ptr_2 < len(array):
            if array[ptr_1] == array[ptr_2]:
                ptr_1 = ptr_2
                ptr_2 += 1
                continue
            else:
                trend = array[ptr_1] > array[ptr_2] if trend == "" else trend
                difference = array[ptr_1] >= array[ptr_2]
                if difference != trend:
                    return False
                ptr_1 = ptr_2
                ptr_2 += 1

    return True


if __name__ == "__main__":
    result = is_monotonic( [-1, -5, -10, -1100, -1100, -1101, -1102, -9001])
    print(result)
