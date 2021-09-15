#문제: 주어진 nums에서 subarray의 합이 k가 되는 모든 경우의 수를 구하여라

from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    cml_sums = []
    tmp_sum = 0
    for num in nums:
        tmp_sum += num
        cml_sums.append(tmp_sum)

    table = {}
    count = 0
    table[0] = [1]
    for idx, cml_sum in enumerate(cml_sums):
        target = cml_sum - k
        if target in table:
            count += len(table[target])

        if cml_sum not in table:
            table[cml_sum] = [idx]
        else:
            table[cml_sum].append(idx)

    return count

print(subarraySum(nums=[6,3,2,5,3,-3],k=10))