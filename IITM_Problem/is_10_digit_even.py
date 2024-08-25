"""Returns True if the number is a 10 digit even number, False otherwise.

Args: 
    n (int): The given number. 

Returns: 
    bool : result as True or False. 

>>> is_ten_digit_even(8769473839)
False
>>> is_ten_digit_even(9289479278)
True
"""


def is_ten_digit_even(n):
    return len(str(n)) == 10 and n % 2 == 0


if __name__ == "__main__":
    result = is_ten_digit_even(8769473839)
    print(result)
    result = is_ten_digit_even(9289479278)
    print(result)
