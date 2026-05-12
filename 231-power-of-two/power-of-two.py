class Solution(object):
    def isPowerOfTwo(self, n):
        import math
        if n <= 0:
            return False
        log_val = math.log(n, 2)
        return 2 ** round(log_val) == n
        