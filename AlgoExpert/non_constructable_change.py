""" Given an array of positive integers representing the values of coins in your possession, write a function that
returns the minimum number of change (the minimum sum of money) that you cannot create. the given coins can have
any positive integers and aren't necessarily unique (that is you can have multiple coins of same value)

For example if you are given coins [1,2, 5] the minimum amount of change that you can't create is 4. If you are given no
 coins the minimum number of change that you can't create is 1
"""


def non_constructible_change(coins):
    coins.sort()
    change = 1
    for x in coins:
        if x - change <= 0:
            change += x
        else:
            break

    return change


if __name__ == "__main__":
    result = non_constructible_change([5, 7, 1, 1, 2, 3, 22])
    print(result)
