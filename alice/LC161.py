class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if (s[i + 1:] == t[j:]) or (s[i:] == t[j + 1:]) or (s[i + 1:] == t[j + 1:]):
                    return True
                else:
                    return False

        return max(len(s) - i, len(t) - j) == 1