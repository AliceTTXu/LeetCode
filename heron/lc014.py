class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # check if the input is empty
        result = ""
        if strs is None or len(strs) == 0:
            return result

        # start to scan, pick the first one to act as base string
        s = strs[0]

        # walk through all char in the bast string
        for i in range(len(s)):
            # check with all other strings
            for j in range(len(strs)):
                if i >= len(strs[j]) or s[i] != strs[j][i]:
                    return result
            result += s[i]

        return result
