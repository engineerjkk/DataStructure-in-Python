nums=[1,3,7,4,8]
target=5

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)-1):
        if(target==(nums[i]+nums[j])):
            print(nums[i])
            print(nums[j])