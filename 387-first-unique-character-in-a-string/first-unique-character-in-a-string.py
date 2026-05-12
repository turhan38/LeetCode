class Solution(object):
    def firstUniqChar(self, s):
        unique = -1
        size = len(s)
        multiples = []
        for i in range(size):
            if(s[i] not in multiples):
                count = s.count(s[i])
                multiples.append(s[i])
                if(size==1):
                    unique = 1
                elif(count==size):
                    break
                if(count == 1):
                    unique = i
                    break
        return unique