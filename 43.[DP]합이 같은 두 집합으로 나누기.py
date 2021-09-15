#문제: 양의 정수만으로 이루어진 숫자들을 합이 같은 두 subset으로 분류가 가능한지 판별하여라.

from typing import List


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 == 1:
        return False

    half_sum = int(total / 2)

    dp_table = [[False] * (half_sum + 1) for j in range(len(nums) + 1)]

    for rowIdx in range(len(dp_table)):
        dp_table[rowIdx][0] = True

    for rowIdx in range(1, len(dp_table)):
        nth_num = nums[rowIdx - 1]
        prev_row = rowIdx - 1
        for colIdx in range(1, len(dp_table[rowIdx])):
            dp0 = False
            prev_col = colIdx - nth_num
            if 0 <= prev_col:
                dp0 = dp_table[prev_row][prev_col]
            dp1 = dp_table[prev_row][colIdx]

            dp = dp0 or dp1
            dp_table[rowIdx][colIdx] = dp

    return dp_table[-1][-1]  # return last dp table elem



print(canPartition(nums=[2,1,2,3,4]))
