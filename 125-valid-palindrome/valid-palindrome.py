class Solution(object):
    def isPalindrome(self, s):
        s = s.replace(" ", "").lower()
        tempS = "".join(char for char in s if char.isalnum())
        if tempS == tempS[::-1]:
            return True
        else:
            return False

        
        