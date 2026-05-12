class Solution(object):
    def searchInsert(self, nums, target):
        output = len(nums) if target > nums[len(nums)-1] else 0
        try:
            output= nums.index(target)
        except:
            for i in range(len(nums)-1):
                if(target>=nums[i]and target<nums[i+1]):
                    output = i+1
        return output