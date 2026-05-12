class Solution(object):
    def validPalindrome(self, s):
        if s != s[::-1]:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return (
                        s[left:right] == s[left:right][::-1]
                        or s[left + 1 : right + 1] == s[left + 1 : right + 1][::-1]
                    )
                left += 1
                right -= 1
        else:
            return True