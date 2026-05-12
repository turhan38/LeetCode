class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        lNums = len(nums)
        count = 0
        for i in range(lNums-2):
            for j in range(i,lNums-1):
                if(nums[j]-nums[i]==diff):
                    for k in range(j,lNums):
                        if(nums[k]-nums[j]==diff):
                            count+=1
        return count
        