class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        index = 0
        currentMap = {}
        out = 0
        currentSubstring = ''

        for i in xrange(len(s)):
            currentSubstring += s[i]

            if s[i] in currentMap and currentMap[s[i]] >= index:
                index = currentMap[s[i]] + 1

            currentMap[s[i]] = i
            currentSubstring = s[index:i + 1]

            if len(currentSubstring) > out:
                out = len(currentSubstring)

        return out




s = Solution()
print s.lengthOfLongestSubstring("")
print s.lengthOfLongestSubstring("abcabcaa")
print s.lengthOfLongestSubstring("bbbbbb")
print s.lengthOfLongestSubstring("pwwkew")
print s.lengthOfLongestSubstring("abcdefg")
