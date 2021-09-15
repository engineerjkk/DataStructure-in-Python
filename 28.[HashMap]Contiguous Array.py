#문제: 1과 0으로 이루어진 array에서 1과 0의 갯수가 같은 subarray의 최대길이는 몇 인가?

from typing import List


def findMaxLength(nums: List[int]) -> int:
    for idx in range(len(nums)):
        if nums[idx] == 0:
            nums[idx] = -1

    cml_sums = []
    tmp_sum = 0
    for num in nums:
        tmp_sum += num
        cml_sums.append(tmp_sum)

    table = {}
    max_length = 0
    table[0] = [-1]

    for idx, cml_sum in enumerate(cml_sums):
        if cml_sum not in table:
            table[cml_sum] = [idx]
        else:
            table[cml_sum].append(idx)

        indices = table[cml_sum]
        first_idx = indices[0]
        last_idx = indices[-1]
        length = last_idx - first_idx
        max_length = max(max_length, length)

    return max_length

print(findMaxLength(nums=[1,0,1,1,1,0,0,1,1]))