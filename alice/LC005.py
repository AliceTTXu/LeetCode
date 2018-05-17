class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ''

        self.word = s

        max_length = 1
        left = 0
        right = 1
        for i in xrange(1, len(s)):
            odd = self.extend_center(i, i)
            even = self.extend_center(i - 1, i)
            temp_max = max(odd, even)
            if temp_max > max_length:
                max_length = temp_max
                left = i - temp_max / 2
                right = i + (temp_max + 1) / 2

        return s[left:right]
        
    def extend_center(self, left, right):
        l, r = left, right
        while l >= 0 and r < len(self.word) and self.word[l] == self.word[r]:
            l -= 1
            r += 1
        return r - l - 1