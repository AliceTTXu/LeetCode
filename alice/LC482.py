class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        raw = ''.join(S.split('-')).upper()
        i = len(raw)
        out = ''

        while (i - K) >=0:
            out = raw[i - K:i] + '-' + out
            i -= K

        if i > 0:
            out = raw[:i] + '-' + out

        return out[:-1]