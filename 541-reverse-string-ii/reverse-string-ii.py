class Solution(object):
    def reverseStr(self, s, k):
        result = ""
        for i in range(0, len(s), 2 * k):
            chunk = s[i:i + k]
            result += chunk[::-1] + s[i + k:i + 2 * k]
        return result
        