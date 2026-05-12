class Solution(object):
    def sortPeople(self, names, heights):
        heights, names = zip(*sorted(zip(heights, names),reverse=True))
        return names
        