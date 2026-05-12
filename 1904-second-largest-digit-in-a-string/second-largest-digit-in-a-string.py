class Solution(object):
    def secondHighest(self, s):
        firstLargest ,secondLargest = -1,-1
        for i in s:
            if(i.isdigit()):
                i = int(i)
                if(i >firstLargest):
                    secondLargest = firstLargest
                    firstLargest = i
                elif(i >secondLargest and firstLargest != i):
                    secondLargest = i
        return secondLargest
        