class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if not m or not n:
            return 0

        dp = [[0] * m for _ in xrange(n)]

        dp[0] = [1] * m
        for i in xrange(1, n):
            dp[i][0] = 1

        for i in xrange(1, n):
            for j in xrange(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]
