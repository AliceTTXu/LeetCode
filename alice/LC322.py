class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [0] + [-1] * amount
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in xrange(amount + 1):
            if i == 0 or dp[i] == 1:
                continue
            else:
                temp = amount + 1
                for coin in coins:
                    sub_amount = i - coin
                    if sub_amount > 0 and dp[sub_amount] != -1:
                        temp = min(temp, dp[sub_amount] + 1)
                if temp < amount + 1:
                    dp[i] = temp

        return dp[amount]