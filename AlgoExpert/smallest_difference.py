"""Write a function that takes 2 non-empty array of integers, finds a pair of numbers (one from each array) whose
absolute difference is close to zero, and returns an array containing those numbers, with the number from the first
array in the first position.

Note: Absolute difference of two integers is the distance between them on the real number line. For example the distance
between -5 and 5 is 10 and the absolute difference of -5 and -4 is 1

Sample Input
------------
arrayOne = [-1, 5,10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output
-------------
[28, 26]
"""
from typing import List


def smallest_difference(array_one: List[int], array_two: List[int]) -> List[int]:
    least_diff = ""
    pairs = []

    for resource_one in array_one:
        for resource_two in array_two:
            curr_diff = abs(resource_two - resource_one)
            if least_diff == "":
                least_diff = curr_diff
            else:
                if least_diff > curr_diff:
                    pairs.clear()
                    pairs.extend([resource_one, resource_two])
                    least_diff = curr_diff

    return pairs


def smallest_difference_improved_time_complexity(array_one: List[int], array_two: List[int]) -> List[int]:
    array_one.sort()
    array_two.sort()

    print("Array One:", array_one)
    print("Array Two:", array_two)

    array_one_ptr, array_two_ptr = 0, 0
    pairs = []
    least_diff = float("inf")

    while array_one_ptr < len(array_one) and array_two_ptr < len(array_two):
        current_sum = abs(array_one[array_one_ptr] - array_two[array_two_ptr])
        if current_sum < least_diff:
            pairs = [array_one[array_one_ptr], array_two[array_two_ptr]]
            least_diff = current_sum

        if array_one[array_one_ptr] > array_two[array_two_ptr]:
            array_two_ptr += 1
        else:
            array_one_ptr += 1

    return pairs


if __name__ == "__main__":
    # result = smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    # print(result)

    result = smallest_difference_improved_time_complexity([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    print(result)
