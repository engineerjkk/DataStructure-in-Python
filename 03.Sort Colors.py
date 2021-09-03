def sortColors(nums):
    idx0 = 0
    idx2 = len(nums) - 1
    i = 0

    while i <= idx2:
        if nums[i] == 0:
            nums[i], nums[idx0] = nums[idx0], nums[i]
            i += 1
            idx0 += 1
        elif nums[i] == 2:
            nums[i], nums[idx2] = nums[idx2], nums[i]
            idx2 -= 1
        else:
            i += 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)














'''
nums2 = [2,0,2,1,1,0]
nums2.sort()
print(nums2)
'''