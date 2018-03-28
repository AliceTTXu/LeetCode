class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if not p:
            return not s

        first_is_match = bool(s) and (p[0] == s[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_is_match and self.isMatch(s[1:], p))
        else:
            return first_is_match and self.isMatch(s[1:], p[1:])