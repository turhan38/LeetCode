class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        errors = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                errors += 1
        if errors == 0 and len(set(heights)) == 1:
            return 0
        return errors
        