class Solution(object):
    def addToArrayForm(self, num, k):
        num = [str(i) for i in num]
        num = int("".join(num))
        num += k
        return [int(i) for i in str(num)]
        