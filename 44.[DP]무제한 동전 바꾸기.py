#문제: coins에 들어있는 종류의 갯수가 무제한 있을때, amount를 만들수있는 조합의 갯수를 구하여라

from typing import List


def coinChange(amount: int, coins: List[int]) -> int:
    dp_table = [[0] * (amount + 1) for j in range(len(coins) + 1)]

    for rowIdx in range(len(dp_table)):
        dp_table[rowIdx][0] = 1

    for rowIdx in range(1, len(dp_table)):
        coin = coins[rowIdx - 1]
        prev_row = rowIdx - 1
        for colIdx in range(1, len(dp_table[rowIdx])):
            dp0 = 0
            prev_col = colIdx - coin
            if 0 <= prev_col:
                dp0 = dp_table[rowIdx][prev_col]
            dp1 = dp_table[prev_row][colIdx]

            dp = dp0 + dp1
            dp_table[rowIdx][colIdx] = dp

    return dp_table[-1][-1]  # return last dp table elem

print(coinChange(amount=5,coins=[1,2,3]))