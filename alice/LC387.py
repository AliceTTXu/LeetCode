import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        out = -1
        counts = {}
        for x in s:
            counts[x] = counts.get(x, 0) + 1

        indexes = [s.index(x) for x in counts if counts[x] == 1]

        return min(indexes) if indexes else -1
