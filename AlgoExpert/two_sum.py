""" Write a function that takes in  a non-empty array of distinct integers and an integer
representing a target sum. If any two numbers in the input array sum up to the target sum,
the function should return them in an array in any order. If no two numbers sum up to the target
sum, the function should return an empty array.

Note that the target sum has to be trained by summing two different integers in the array;
you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input
------------

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sample Output
-------------
[-1, 11]
"""
from typing import List, Tuple


def two_sum(array: List[int], target: int) -> list[Tuple[int, int]]:
    """
    Brute force method of iterating over the array twice.
    """
    return [
        (array[i], array[j]) for i in range(len(array) - 1)
        for j in range(i + 1, len(array) - 1)
        if array[i] + array[j] == target
    ]


def two_sum_with_pointer_approach(array: List[int], target: int) -> List[Tuple[int, int]]:
    """
    1. sort the array
    2. set the pointer at 2 ends.
    3. add the 2 pointers from both ends.
        i. if the sum is greater than target then move pointer left
        ii. if the sum is less than target then move the pointer to right
        iii. if the two pointers cross each other exit.
    """
    array.sort()
    pairs = []
    left_ptr = 0
    right_ptr = len(array) - 1

    while True:
        if left_ptr < right_ptr:
            if array[left_ptr] + array[right_ptr] == target:
                pairs.append((array[left_ptr], array[right_ptr]))
                right_ptr -= 1
            elif array[left_ptr] + array[right_ptr] > target:
                right_ptr -= 1
            elif array[left_ptr] + array[right_ptr] < target:
                left_ptr += 1
        else:
            break

    return pairs


def two_sum_with_lookup(array: List[int], target: int) -> List[Tuple[int, int]]:
    """Use a memory based lookup approach leveraging hash algorithm to have faster lookup and
    identify the pairs.
    """
    lookup = {}
    pairs = []
    for rec in array:
        compliment_of_number = target - rec
        if rec in lookup:
            pairs.append((rec, compliment_of_number))
        else:
            lookup[compliment_of_number] = rec

    return pairs


if __name__ == "__main__":
    result = two_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(result)

    result = two_sum_with_pointer_approach([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(result)

    result = two_sum_with_lookup([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(result)
