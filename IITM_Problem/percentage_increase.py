"""Calculate the percentage increase from the original value to the new value.

Args:
    original (float): The original value.
    new (float): The new value.

Returns:
    float: The percentage increase.

Examples:
>>> percentage_increase(50, 75)
50.0
>>> percentage_increase(80, 100)
25.0
"""


def percentage_increase(original, new):
    return ((new - original) / original) * 100


if __name__ == "__main__":
    result = percentage_increase(50, 75)
    print(result)
    result = percentage_increase(80, 100)
    print(result)
