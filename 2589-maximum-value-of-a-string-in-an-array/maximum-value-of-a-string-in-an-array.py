class Solution(object):
    def maximumValue(self, strs):
        maxV = 0
        for i in strs:
            if(i.isdigit()):
                if(int(i)>maxV):
                    maxV = int(i)
            else:
                iLen = len(i)
                if(iLen>maxV):
                    maxV = iLen
        return maxV