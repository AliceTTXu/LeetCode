class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        strInt = str(num)
        digits = len(strInt)

        out = ''

        for i in xrange(digits):
            oneDigit = int(strInt[i])
            scale = 10**(digits - i - 1)
            if oneDigit == 0:
                out += ''
            elif oneDigit >= 1 and oneDigit <= 3:
                out += ''.join([mapping[scale] for i in range(oneDigit)])
            elif oneDigit == 4:
                out = out + mapping[scale] + mapping[5 * scale]
            elif oneDigit == 5:
                out += mapping[5 * scale]
            elif oneDigit >= 6 and oneDigit <= 8:
                out = out + mapping[5 * scale] + ''.join([mapping[scale] for i in range(oneDigit - 5)])
            elif oneDigit == 9:
                out = out + mapping[scale] + mapping[10 * scale]

        return out
      

s = Solution()
print s.intToRoman(1)
print s.intToRoman(18)
print s.intToRoman(199)
print s.intToRoman(1437)
print s.intToRoman(3333)
print s.intToRoman(3999)