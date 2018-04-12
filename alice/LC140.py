class Solution(object):
    def wordBreak(self, s, wordDict):
        self.wordDictSet = set(wordDict)
        self.sol_dict = {len(s): ['']}
        return self.wordBreak_rec(s, 0)

    def wordBreak_rec(self, s, index):
        if index in self.sol_dict:
            return self.sol_dict[index]

        out = []
        for i in range(index + 1, len(s) + 1):
            if s[index:i] in self.wordDictSet:
                for tail in self.wordBreak_rec(s, i):
                    out.append(s[index:i] + (tail and ' ' + tail))
        self.sol_dict[index] = out

        return self.sol_dict[index]


    def wordBreak_dp(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        wordDictSet = set(wordDict)

        dp = [['']] + [[] for _ in range(len(s))]

        for i in xrange(len(s)):
            for j in xrange(i + 1):
                temp = dp[j] and (s[j:i + 1] in wordDictSet)
                if temp:
                    dp[i + 1].extend([x + ' ' + s[j:i + 1] for x in dp[j]])

        return [x[1:] for x in dp[-1]]

s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])