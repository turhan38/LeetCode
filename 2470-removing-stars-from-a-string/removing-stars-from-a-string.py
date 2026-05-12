class Solution(object):
    def removeStars(self, s):
        mainS = []
        for i in s:
            if i == "*":
                mainS.pop()
            else:
                mainS.append(i)
        return "".join(mainS)