"""Move elements to end:
You are given an array of integers and integer. Write a function that moves all instance of that integer in the array
to the end of the array and returns the array. The function should perform this in place. (i.e it should mutate the
input array and doesn't need to maintain the order of the other .

Sample Input
------------
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output
-------------
[1, 3, 4, 2, 2, 2, 2, 2]
"""


def move_element_to_end(array, to_move):
    start, end = 0, len(array) - 1
    while start < end:
        if array[start] == to_move:
            array[start], array[end] = array[end], array[start]
            end -= 1
        else:
            start += 1
    return array


if __name__ == "__main__":
    result = move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
    print(result)
