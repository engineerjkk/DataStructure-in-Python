#문제: coins에 주어진 동전가니고 amount를 만들기 위한 최소한의 동전의 갯수는 몇개인가?

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    MAX_COST = 999999999
    dp_array = [-1] * (amount + 1)
    dp_array[0] = 0

    for idx in range(amount + 1):
        if dp_array[idx] != -1:
            continue

        crnt_min = MAX_COST
        for coin in coins:
            last_idx = idx - coin
            if last_idx < 0:
                continue
            last_cost = dp_array[last_idx]
            if last_cost == -1:
                continue
            cost = last_cost + 1
            crnt_min = min(cost, crnt_min)

        dp_array[idx] = -1 if crnt_min == MAX_COST else crnt_min

    return dp_array[amount]


print(coinChange(coins=[2, 3, 5], amount=10))