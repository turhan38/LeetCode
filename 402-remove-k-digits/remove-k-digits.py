class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack[:-k] if k > 0 else stack
        return "".join(stack).lstrip("0") or "0"
        