class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        cleanStr = str.strip()
        if not cleanStr:
            return 0

        sign = 1
        if cleanStr[0] == '-':
            sign = -1
            cleanStr = cleanStr[1:]
        if cleanStr[0] == '+':
            cleanStr = cleanStr[1:]

        num = 0
        for x in cleanStr:
            if x.isdigit():
                num = num * 10 + ord(x) - ord('0')
            else:
                break
        return min(max(sign * num, -2147483648), 2147483647)

s = Solution()
print s.myAtoi("    -2313")