"""Write a function that takes in a non-empty array of distinct integers and an integer representing target sum.
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array
of the triplet. The numbers in each triplet should be ordered in ascending order, and the triplet themselves should be
ordered in ascending order w.r.t the numbers they hold

if no 3 numbers add up to target sum, the function should return an empty array.

Sample Input
------------
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample Output
-------------
[[-8,2,6], [-8,3,5], [-6,1,5]]
"""
from typing import List


def three_number_sum(array: List[int], target_sum: int) -> List[List[int]]:
    triplets = []
    array.sort()
    for pos, pivot in enumerate(array):
        l_ptr = pos + 1
        r_ptr = len(array) - 1
        while l_ptr < len(array):
            current_sum = pivot + array[l_ptr] + array[r_ptr]
            if current_sum == target_sum:
                triplets.append([pivot, array[l_ptr], array[r_ptr]])
                l_ptr += 1
                r_ptr -= 1
            elif current_sum > target_sum:
                r_ptr -= 1
            else:
                l_ptr += 1

            if l_ptr >= r_ptr:
                break

    return triplets


if __name__ == "__main__":
    result = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    print(result)
