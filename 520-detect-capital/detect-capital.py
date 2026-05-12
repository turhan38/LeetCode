class Solution(object):
    def detectCapitalUse(self, word):
        if word[:].isupper() or (word[0].isupper() and word[1:].islower())or word[:].islower():
            return True
        else:
            return False