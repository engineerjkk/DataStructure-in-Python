def moveZeroes(nums):
    prev_idx = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            hold = nums[prev_idx]
            nums[prev_idx] = nums[i]
            nums[i] = hold
            prev_idx += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)

# 0이아닌 상수에서만 if문안으로 들어가는데