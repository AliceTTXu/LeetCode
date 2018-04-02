class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not p:
            return not s

        level = [0]

        for x in p:
            if x == '*':
                level = range(level[0], len(s) + 1)
            else:
                level = [y + 1 for y in level if y < len(s) and (x == '?' or s[y] == x)]
                if not level:
                    return False

        return level[-1] == len(s)
 
    def isMatch_slow(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if not p:
            return not s

        if set(list(p)) == set('*'):
            return True

        if not s:
            return False

        first_is_match = (s[0] == p[0] or p[0] == '?')

        if p[0] == "*":
            return self.isMatch(s[1:], p) or self.isMatch(s[1:], p[1:]) or self.isMatch(s, p[1:])
        else:
            return first_is_match and self.isMatch(s[1:], p[1:])

s = Solution()
print s.isMatch("abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab", "*aabb***aa**a******aa*")
print s.isMatch("dsfkh", "*")
print s.isMatch("absdjkwd", "a*b")
print s.isMatch("sdfhk", "a")