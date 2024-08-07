"""Sorted Squared Array
Write a function that takes in a non-empty array of integers that are sorted in ascending order returns a new array
of the same length with squares of original integers also sorted in ascending order.

Sample Input
------------
array = [1, 2, 3, 5, 6, 8, 9]

Sample Output
-------------
[1, 4, 9, 25, 36, 64, 81]
"""


def sorted_squared_array(array):
    return sorted([rec * rec for rec in array])


def sorted_squared_array_using_map(array):
    return sorted(list(map(lambda rec: rec * rec, array)))


if __name__ == "__main__":
    result = sorted_squared_array([1, 2, 3, 5, 6, 8, 9])
    print(result)

    result = sorted_squared_array_using_map([1, 2, 3, 5, 6, 8, 9])
    print(result)