#문제: 주어진 Array에서 최대곱 from typing import List Maximum Subarray를 계산하여라
# 각 element의 곱샘이 최대가 되는 subarray를 찾아라
from typing import List


def maxProduct(nums: List[int]) -> int:
    max_dp = [nums[0]]
    min_dp = [nums[0]]

    for idx in range(1, len(nums)):
        prev_idx = idx - 1

        num = nums[idx]
        cand0 = num
        cand1 = max_dp[prev_idx] * num
        cand2 = min_dp[prev_idx] * num

        max_val = max(cand0, cand1, cand2)
        min_val = min(cand0, cand1, cand2)

        max_dp.append(max_val)
        min_dp.append(min_val)

    max_product = max(max_dp)
    return max_product


print(maxProduct(nums=[3, -2, 1, 0, -8, -9]))