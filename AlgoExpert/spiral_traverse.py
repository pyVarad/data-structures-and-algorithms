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

def spiral_traverse(array):
    spiral = []
    if len(array) > 0:
        num_cols = len(array[0])
        num_rows = len(array)

        start_row, last_row = 0, num_rows
        start_col, last_col = 0, num_cols

        while start_row <= last_row and start_col <= last_row:
            for col in range(start_col, last_col + 1):
                spiral.append(col)
            start_row += 1

            if start_row > last_row:
                break

            for row in range(start_row, last_row + 1):
                spiral.append(row)
            last_col -= 1

            if start_col > last_col:
                break

            for col in reversed(range(start_col, last_col+ 1)):
                spiral.append(col)
            last_row -= 1

            for row in reversed(range(start_row, last_row + 1)):
                spiral.append(row)
            start_col += 1

    return spiral

if __name__ == "__main__":
    array = [
        [1, 2, 3, 4],
        [12 ,13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    res = spiral_traverse(array)
    print(res)