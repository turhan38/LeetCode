class Solution(object):
    def divide(self, dividend, divisor):
        counter = 0
        isNegative  = (divisor<0 or dividend<0)and not (divisor<0 and dividend<0)
        divisor = abs(divisor)
        dividend = abs(dividend)
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            counter += multiple
        return min(max(-2147483648, counter if not isNegative else -counter), 2147483647)