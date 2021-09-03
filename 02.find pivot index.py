def pivotIndex(nums):
    sums = sum(nums)
    leftSum = 0
    rightSum = sums

    pastPivotNum = 0
    for i in range(0, len(nums)):
        num = nums[i]
        rightSum = rightSum - num
        leftSum = leftSum + pastPivotNum
        if (leftSum == rightSum):
            return i
        pastPivotNum = num
    return -1

nums = [1,7,3,6,5,6]
result=pivotIndex(nums)
print(result)


