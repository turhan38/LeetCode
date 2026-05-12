class Solution(object):
    def permuteUnique(self, nums):
        from itertools import permutations
        return(list(set(permutations(nums))))
        
        