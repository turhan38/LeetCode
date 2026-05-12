class Solution(object):
    def isIsomorphic(self, s, t):
        tempListS, tempListT = {},{}
        for charS, charT in zip(s, t):
            if (charS in tempListS and tempListS[charS] != charT) or (charT in tempListT and    tempListT[charT] != charS):
                return False
            tempListS[charS] = charT
            tempListT[charT] = charS
        return True