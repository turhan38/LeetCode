class Solution(object):
    def customSortString(self, order, s):
        return "".join(sorted(s, key=lambda x: order.index(x) if x in order else len(order)))
        