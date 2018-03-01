class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        counts = {0: 1, 1: 1}

        for i in xrange(2, n + 1):
        	counts[i] = sum([counts[j] * counts[i - j - 1] for j in range(i)])

        return counts[n]

s = Solution()
print s.numTrees(1)
print s.numTrees(2)
print s.numTrees(3)
print s.numTrees(4)
print s.numTrees(5)