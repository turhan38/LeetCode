class Solution(object):
    def singleNumber(self, nums):
        answers = []
        nums.sort()
        i,lenNums = 0,len(nums)
        while i<lenNums:
            if(i == lenNums-1 or nums[i]!=nums[i+1]):
                answers.append(nums[i])
                if(len(answers)==2):
                    return answers
                i+=1
            else:
                i+=2
        