#양수로 주어진 nums중에서 두 수의 합이 target이 되는 index들을 return하여라

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}

    for idx, num in enumerate(nums):
        match_num = target - num
        match_idx = hash_table.get(match_num)

        if match_idx is not None:
            return [idx, match_idx]

        hash_table[num] = idx

indices = twoSum(nums = [13,7,5,1,3,2],target=10)
print(indices)