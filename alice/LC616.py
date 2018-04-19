class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        
        lens = set()
        dict = set(dict)
        for x in dict:
            lens.add(len(x))

        b = [False for _ in range(len(s))]

        for i in xrange(len(s)):
            for l in lens:
                if s[i:i + l] in dict:
                    b[i:i + l] = [True] * l

        out = ''
        for i in xrange(len(s)):
            if b[i] == True:
                if i == 0 or b[i - 1] == False:
                    out += '<b>'
                out += s[i]
                if i == len(s) - 1 or b[i + 1] == False:
                    out += '</b>'
            else:
                out += s[i]
                
        return out