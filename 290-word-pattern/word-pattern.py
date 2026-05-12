class Solution(object):
    def wordPattern(self, pattern, s):
        patternArray = []
        s = s.split()
        if len(pattern)!= len(s):
            return False
        for i in pattern:
            if i not in patternArray:
                patternArray.append(i)
        clearArray = []
        for k in s:
            if k not in clearArray:
                clearArray.append(k)
        if len(patternArray) != len(clearArray):
            return False
        else:
            for k in range(len(s)):
                s[k] = str(patternArray[clearArray.index(s[k])])
                if s[k] != pattern[k]:
                    return False
            return True
        