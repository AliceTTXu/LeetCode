class Solution(object):
    def wordPatternMatch(self, p, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        if not p and not s:
            return True

        if not p or len(s) < len(p):
            return False
        
        mapping = {}
        seen = set()

        return self.DFS(p, 0, s, 0, mapping, seen)

    def DFS(self, p, p_index, s, s_index, mapping, seen):
        if p_index == len(p) and s_index == len(s):
            return True

        if p_index == len(p) or s_index == len(s):
            return False

        pp = p[p_index]
        if pp in mapping:
            temp = mapping[pp]
            if temp == s[s_index: s_index + len(temp)]:
                return self.DFS(p, p_index + 1, s, s_index + len(temp), mapping, seen)
            else:
                return False
        else:
            for i in xrange(s_index, len(s) - (len(p) - p_index - 1)):
                temp = s[s_index: i + 1]
                if temp in seen:
                    continue
                mapping[pp] = temp
                seen.add(temp)
                if self.DFS(p, p_index + 1, s, i + 1, mapping, seen):
                    return True
                del mapping[pp]
                seen.remove(temp)
            return False