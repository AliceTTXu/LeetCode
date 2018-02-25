class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) < 1 or s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        else:
            p0 = 1
            p1 = 1
            for i in range(1, len(s)):
                if int(s[i]) >= 1:
                    x = p1
                else:
                    x = 0
                if int(s[i - 1: i + 1]) <= 26 and s[i - 1] != '0':
                    y = p0
                else:
                    y = 0
                p0 = p1
                p1 = x + y

        return p1

s = Solution()
print s.numDecodings('110')