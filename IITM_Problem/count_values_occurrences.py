"""Count the number of occurrences of each value in the dictionary.

Args:
    d (dict): The input dictionary.

Returns:
    dict: A dictionary where the keys are the values from the input dictionary, 
    and the values are their occurrence counts.

Examples:
>>> count_values_occurrences({'a': 1, 'b': 2, 'c': 1})
{1: 2, 2: 1}
>>> count_values_occurrences({1: 'x', 2: 'y', 3: 'x'})
{'x': 2, 'y': 1}
"""


def count_values_occurrences(d):
    ref = {}
    for k, v in d.items():
        cnt = ref.get(v, 0) + 1
        ref[v] = cnt
    return ref


if __name__ == "__main__":
    result = count_values_occurrences({'a': 1, 'b': 2, 'c': 1})
    print(result)
    result = count_values_occurrences({1: 'x', 2: 'y', 3: 'x'})
    print(result)
