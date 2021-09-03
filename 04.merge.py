def merge(nums1, m, nums2, n):
    wIdx = len(nums1) - 1
    nums1Idx = m - 1
    nums2Idx = m - 1

    while 0 <= nums1Idx and 0 <= nums2Idx:
        num1 = nums1[nums1Idx]
        num2 = nums2[nums2Idx]
        if (num1 <= num2):
            nums1[wIdx] = num2
            nums2Idx -= 1
            wIdx -= 1
        else:
            nums1[wIdx] = num1
            nums1Idx -= 1
            wIdx -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print(nums1)


'''
nums2 = [2,0,2,1,1,0]
nums2.sort()
print(nums2)
'''