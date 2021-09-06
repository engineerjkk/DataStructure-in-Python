def findPeakElement(nums):
    left=0
    right=len(nums)-1

    while(left<right):
        pivot=int((left+right)/2)
        num=nums[pivot]
        nextNum=nums[pivot+1]

        if (num<nextNum):
            left=pivot+1
        else:
            right=pivot
    return left


nums = [1,2,1,3,5,6,4]

answer=findPeakElement(nums)

print(answer)

