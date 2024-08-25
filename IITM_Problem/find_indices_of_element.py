"""Find all indices of an element in a list.

Args:
    l (list): The input list.
    elem: The element to find.

Returns:
    list: A list of indices where the element is found.

Examples:
>>> find_indices_of_element([1, 2, 3, 2, 4], 2)
[1, 3]
>>> find_indices_of_element(['a', 'b', 'a', 'c'], 'a')
[0, 2]
"""


def find_indices_of_element(l, elem):
    return [pos for pos, element in enumerate(l) if element == elem]


if __name__ == "__main__":
    result = find_indices_of_element([1, 2, 3, 2, 4], 2)
    print(result)

    result = find_indices_of_element(['a', 'b', 'a', 'c'], 'a')
    print(result)
