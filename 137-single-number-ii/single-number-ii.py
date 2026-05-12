class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        i,lNums =0, len(nums)
        while i<lNums:
            if(i == lNums-1 or nums[i]!=nums[i+1]):
                return nums[i]
            else:
                i+=3
        