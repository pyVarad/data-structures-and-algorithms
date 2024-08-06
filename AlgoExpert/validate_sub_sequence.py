"""Given two non-empty array of integers, write a function that determines whether the second array is a subsequence
of the first one. For instance [1,3,4] form a subsequence of the array [1,2,3,4] and so do the numbers [2,4]. Note
that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input
------------
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]


Sample Output
-------------
true
"""
from typing import List


def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:
    main_seq_ptr_position = 0
    sub_seq_ptr_position = 0

    while True:
        if array[main_seq_ptr_position] == sequence[sub_seq_ptr_position]:
            main_seq_ptr_position += 1
            sub_seq_ptr_position += 1
        else:
            main_seq_ptr_position += 1

        if sub_seq_ptr_position == len(sequence):
            return True
        elif main_seq_ptr_position == len(array):
            return False


if __name__ == "__main__":
    result = is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    print(result)
