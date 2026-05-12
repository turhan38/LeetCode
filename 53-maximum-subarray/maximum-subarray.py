class Solution(object):
    def maxSubArray(self, nums):
        maxC = nums[0]
        maxG = nums[0]
        for i in range(1, len(nums)):
            maxC = max(nums[i], maxC + nums[i])
            if maxC > maxG:
                maxG = maxC
        return maxG

        