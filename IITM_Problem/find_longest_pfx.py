"""Find the longest common prefix among the given words of the sentence.

Args:
    sentence (str): A string of space sepearated words.
Returns:
    str: longest prefix.
"""


def find_longest_pfx(sentence):
    ele_length = sorted(list(map(len, sentence.split(" "))))
    if len(ele_length) > 0:
        traverse_len = ele_length[0]
    else:
        traverse_len = 0

    pfx_array = []
    pos = 0
    while traverse_len:
        char_to_check = sentence.split(" ")[0][pos]
        if len(set([rec[pos] for rec in sentence.split(" ")])) > 1:
            break
        pfx_array.append(char_to_check)
        traverse_len -= 1
        pos += 1

    return "".join(pfx_array)


if __name__ == "__main__":
    print(find_longest_pfx('flower flow flight'))
