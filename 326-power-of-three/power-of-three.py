class Solution(object):
    def isPowerOfThree(self, n):
        import math
        if n <= 0:
            return False
        log_val = math.log(n, 3)
        return 3 ** round(log_val) == n
        