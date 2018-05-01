class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if n == 0 or k == 0:
            return 0

        if n == 1:
            return k

        same = k
        diff = k * (k - 1)

        for i in xrange(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)

        return same + diff