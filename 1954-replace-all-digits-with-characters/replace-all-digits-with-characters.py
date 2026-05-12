class Solution(object):
    def replaceDigits(self, s):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
        s = list(s)
        for i in range(len(s)):
            if(s[i]not in alphabet):
                s[i] = alphabet[alphabet.index(s[i-1])+int(s[i])]
        s = "".join(s)
        return s
            