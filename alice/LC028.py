class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """


        
        haystackLength = len(haystack)
        needleLength = len(needle)

        if needleLength > haystackLength:
        	return -1

        i = 0

        while i <= haystackLength - needleLength:
        	if haystack[i:i + needleLength] == needle:
        		return i
        	i += 1

        return -1

s = Solution()
print s.strStr("hello", "ll")
print s.strStr("", "")
print s.strStr("apple", "ll")
print s.strStr("apple", "applepple")
print s.strStr("a", "a")
