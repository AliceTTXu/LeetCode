class Solution(object):
    def longestValidParentheses_dp(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        dp = [0 for i in range(len(s))]

        for i in xrange(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i - 2] + 2
                else:
                    if (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == '(':
                        if (i - dp[i - 1] - 1) == 0:
                            pre = 0
                        else:
                            pre = dp[i - dp[i - 1] - 2]
                        dp[i] = pre + dp[i - 1] + 2

        return dp[-1]

    def longestValidParentheses_stack(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = [-1]
        temp_max = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    temp_max = max(temp_max, i - stack[-1])

        return temp_max

    def longestValidParentheses_greedy(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = right = 0
        temp_max = 0

        for x in s:
            print left, right
            if x == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = right = 0
            if right == left:
                temp_max = max(temp_max, left * 2)

        if left == right:
            return temp_max

        left = right = 0

        for x in s[::-1]:
            if x == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left = right = 0
            if right == left:
                temp_max = max(temp_max, left * 2)

        return temp_max

s = Solution()
print s.longestValidParentheses("(()())")