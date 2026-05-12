class Solution(object):
    def numberOfSpecialChars(self, word):
        lowerSet = set()
        upperSet = set()
        special_count = 0
        for char in word:
            if char.isupper():
                upperSet.add(char)
            elif char.islower():
                upperChar = char.upper()
                lowerSet.add(upperChar)
        return len(upperSet.intersection(lowerSet))
                