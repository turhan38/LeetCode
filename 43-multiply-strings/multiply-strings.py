class Solution(object):
    def multiply(self, num1, num2):
        num1 = [int(digit) for digit in num1]
        num2 = [int(digit) for digit in num2]
        result = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                mul = num1[i] * num2[j]
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]
                result[pos1] += total // 10
                result[pos2] = total % 10
        result_str = ''.join(map(str, result)).lstrip('0')
        return result_str if result_str else '0'
        