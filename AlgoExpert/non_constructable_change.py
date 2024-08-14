""" Given an array of positive integers representing the values of coins in your possession, write a function that
returns the minimum number of change (the minimum sum of money) that you cannot create. the given coins can have
any positive integers and aren't necessarily unique (that is you can have multiple coins of same value)

For example if you are given coins [1,2, 5] the minimum amount of change that you can't create is 4. If you are given no
 coins the minimum number of change that you can't create is 1
"""


def non_constructible_change(coins):
    coins.sort()
    minimum_coin_sum = 0
    counter_pos = 0
    while counter_pos < len(coins) - 1:
        minimum_coin_sum += coins[counter_pos]
        counter_pos += 1

    return minimum_coin_sum + 1


if __name__ == "__main__":
    result = non_constructible_change([5, 7, 1, 1, 2, 3, 22])
    print(result)
