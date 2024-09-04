"""Write a function that takes in a "n x m" two-dimensional array (that can be square shaped when n = m) and returns a
one-dimensional array of all the elements in spiral-order.

Spiral order starts in the top left corner of the two-dimensional array, goes to the right, and proceeds in spiral
pattern all the way until every element has been visited.

Sample Input
------------
array = [
    [1, 2, 3, 4],
    [12 ,13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

Sample Output
-------------
[1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""
from typing import List


def spiral_traverse(array: List[List[int]]) -> List[int]:
    spiral = []
    if len(array) > 0:
        num_cols = len(array[0])
        num_rows = len(array)

        start_row, last_row = 0, num_rows
        start_col, last_col = 0, num_cols

        while start_row <= last_row and start_col <= last_row:
            for col in range(start_col, last_col - 1):
                spiral.append(array[start_row][col])
                print("Inside Col forward iteration: ", start_col, last_col - 1)

            for row in range(start_row, last_row - 1):
                spiral.append(array[row][last_col - 1])
                print("Inside row downward iteration: ", start_row, last_row - 1)


            for col in range(last_col - 1, start_col, -1):
                spiral.append(array[last_row - 1][col])
                print("Inside Col reverse iteration: ", last_col - 1, start_col)


            for row in range(last_row - 1, start_row, -1):
                spiral.append(array[row][start_col])
                print("Inside row upward iteration: ", last_row - 1, start_row)

            last_row -= 1
            last_col -= 1
            start_row += 1
            start_col += 1


    return spiral


if __name__ == "__main__":
    array = [
            [27, 12, 35, 26],
            [25, 21, 94, 11],
            [19, 96, 43, 56],
            [55, 36, 10, 18],
            [96, 83, 31, 94],
            [93, 11, 90, 16]
        ]

    res = spiral_traverse(array)
    print(res)


# [27, 12, 35, 26, 11, 56, 18, 94, 16, 90, 11, 93, 96, 55, 19, 25, 21, 94, 43, 10, 31, 83, 36, 96]
# [27, 12, 35, 26, 11, 56, 18, 94, 31, 83, 96, 55, 19, 25, 21, 94, 43, 10, 36, 96]