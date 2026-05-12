class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)):
            if (i+1) not in nums:
                return i+1
        
        return 0