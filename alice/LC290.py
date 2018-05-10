class Solution(object):
    def wordPattern(self, p, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        s = s.split(' ')
        if len(s) != len(p):
            return False
        
        mapping = {}
        seen = set()
        for pp, ss in zip(p, s):
            if pp not in mapping:
                if ss not in seen:
                    mapping[pp] = ss
                    seen.add(ss)
                else:
                    return False
            else:
                if mapping[pp] != ss:
                    return False
        
        return True
                