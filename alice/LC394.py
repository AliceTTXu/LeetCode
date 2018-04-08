class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ''

        out = ''
        num = []

        for i in range(len(s)):                
            if 0 <= ord(s[i]) - ord('0') <= 9:
                num.append(s[i])
            elif s[i] == '[':
                right = self.find_right(s, i + 1)
                return int(''.join(num)) * self.decodeString(s[i + 1:right]) \
                    + self.decodeString(s[right + 1:])
            else:
                return s[i] + self.decodeString(s[i + 1:])


    def find_right(self, s, start):
        left = 1
        for i in xrange(start, len(s)):
            if s[i] == '[':
                left += 1
            elif s[i] == ']':
                left -= 1
            if left == 0:
                return i
