"""Find all the unique common charecters present in the given words
and return them as a string in ascending order.

Arg:
    word1 (str) : Input string. 
    word2 (str) : Input string. 

Returns: 
    str: string of unique common charecters arranged in ascending order. 

>>> common_chars('apple', 'ball')
'al'
>>> common_chars('abcde', 'edfci')
'cde'
"""


def common_chars(word1, word2):
    return "".join(sorted(set(word1).intersection(set(word2))))


if __name__ == "__main__":
    result = common_chars('apple', 'ball')
    print(result)
    result = common_chars('abcde', 'edfci')
    print(result)
