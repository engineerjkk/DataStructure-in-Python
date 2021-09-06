nums=[1,3,7,4,8]
target=5
left=0
right=len(nums)-1
nums.sort()
for i in range (0, len(nums)):
    small=nums[left]
    big=nums[right]
    if((small+big)>target):
        right=right-1
    elif ((small+big)==target):
        print(small)
        print(big)
        right = right - 1


# 남은 과제 3sum, 4sum