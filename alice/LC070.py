class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0] * (n + 1)

        for i in xrange(n + 1):
            if i == 0 or i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]