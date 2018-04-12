class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        wordDictSet = set(wordDict)
        dp = [True] + [False] * len(s)

        for i in xrange(len(s)):
            for j in xrange(i + 1):
                dp[i + 1] = dp[j] and (s[j:i + 1] in wordDictSet)
                if dp[i + 1]:
                    break

        return dp[-1]