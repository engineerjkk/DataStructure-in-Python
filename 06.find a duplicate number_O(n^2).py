nums=[1,2,3,4,2]
empty=[]
for i in range (0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
            empty.append(nums[i])

print(empty)