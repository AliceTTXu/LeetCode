class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        alpha = len(s) / (numRows + numRows - 2)
        beta = len(s) % (numRows + numRows - 2)

        plusOneTo = min(beta, numRows)
        plusTwoFrom = numRows - max(beta - numRows, 0)

        out = ''

        for i in xrange(numRows):
            if i == 0:
                out += ''.join([s[j * (numRows + numRows - 2)] for j in xrange(alpha + min(1, plusOneTo))])
            elif i == numRows - 1:
                out += ''.join([s[j * (numRows + numRows - 2) + (numRows - 1)] for j in xrange(alpha + plusOneTo / numRows)])
            else:
                for j in xrange(alpha):
                    out += s[j * (numRows + numRows - 2) + i]
                    out += s[j * (numRows + numRows - 2) + (numRows + numRows - 2 - i)]
                if i <= plusOneTo - 1:
                    out += s[alpha * (numRows + numRows - 2) + i]
                if i >= plusTwoFrom - 1:
                    out += s[alpha * (numRows + numRows - 2) + (numRows + numRows - 2 - i)]

        return out

    def convert2(self, s, numRows):

        if numRows <= 1 or numRows >= len(s):
            return s

        tempOut = ['' for i in range(numRows)]
        index = 0
        direction = 1

        for x in s:
            tempOut[index] += x
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index += direction

        return ''.join(tempOut)


s = Solution()
print s.convert2("PAYPALISHIRING", 3)
print s.convert2("PAYPALISHIRING", 5)
print s.convert2("PAYPALISHIRING", 1)
print s.convert2("", 3)