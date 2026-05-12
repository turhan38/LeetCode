class Solution(object):
    def nthUglyNumber(self, n):
        uglyNumbers = [1]
        idx2 = idx3 = idx5 = 0 
    
        for _ in range(1, n):
            nextUgly = min(uglyNumbers[idx2] * 2, uglyNumbers[idx3] * 3, uglyNumbers[idx5] * 5)
            uglyNumbers.append(nextUgly)
            if nextUgly == uglyNumbers[idx2] * 2:
                idx2 += 1
            if nextUgly == uglyNumbers[idx3] * 3:
                idx3 += 1
            if nextUgly == uglyNumbers[idx5] * 5:
                idx5 += 1
        return uglyNumbers[-1]
        