nums=[1,2,3,4,2]

for i in range(0,len(nums)):
    if(nums[i]<0):
        print(-nums[i])
    a=nums[i]
    nums[a]=-nums[a]