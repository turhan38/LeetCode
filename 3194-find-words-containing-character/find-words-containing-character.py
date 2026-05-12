class Solution(object):
    def findWordsContaining(self, words, x):
        indexes = []
        for i in range(len(words)):
            if x in words[i]:
                indexes.append(i)
        return indexes
        