class Solution(object):
    def findTheDifference(self, s, t):
        notNew = []
        for i in t:
            if i not in notNew:
                if s.count(i) != t.count(i):
                    return i
                else:
                    notNew.append(i)
        