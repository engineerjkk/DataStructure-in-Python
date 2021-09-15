#문제: n개의 계단을 오르고자 한다. 한번에 1개, 2개씩의 계단을 오를수 있을때 총 몇가지 방벙으로 계단을 오를 수 있는가?
from typing import List


def climbStairs(n: int) -> int:
    dp_array = [0, 1, 2]

    if n < len(dp_array):
        return dp_array[n]

    for i in range(3, n + 1):
        ith_way = dp_array[i - 1] + dp_array[i - 2]
        dp_array.append(ith_way)
    return dp_array[n]

print(climbStairs(7),'ways')