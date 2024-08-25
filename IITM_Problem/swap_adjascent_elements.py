"""Swap every pair of adjacent elements in the tuple.

Args:
    t (tuple): A tuple of even length.

Returns:
    tuple: A new tuple with adjacent elements swapped.

Examples:
>>> swap_adjacent_elements((1, 2, 3, 4, 5, 6))
(2, 1, 4, 3, 6, 5)
>>> swap_adjacent_elements(('a', 'b', 'c', 'd'))
('b', 'a', 'd', 'c')
"""


def swap_adjacent_elements(t):
    i, j = 0, 1
    while j < len(t):
        t[i], t[j] = t[j], t[i]
        i += 2
        j += 2
    return t


if __name__ == "__main__":
    result = swap_adjacent_elements([1, 2, 3, 4, 5, 6])
    print(result)

    result = swap_adjacent_elements(['a', 'b', 'c', 'd'])
    print(result)
