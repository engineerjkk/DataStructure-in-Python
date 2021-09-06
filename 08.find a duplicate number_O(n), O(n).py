nums=[1,2,3,4,2]
empty=[]
for i in range (0,len(nums)):
    if not nums[i] in empty:
        empty.append(nums[i])
    else:
        print(nums[i])

