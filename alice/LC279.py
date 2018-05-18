class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0]

        while len(dp) <= n:
            temp_min = len(dp)
            i = 1
            while i * i <= len(dp):
                temp_min = min(temp_min, dp[len(dp) - i * i] + 1)
                i += 1
            dp.append(temp_min)

        return dp[n]