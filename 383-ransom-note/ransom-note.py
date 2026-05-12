class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            else:
                magazine = magazine.replace(ransomNote[i], "", 1)
        return True