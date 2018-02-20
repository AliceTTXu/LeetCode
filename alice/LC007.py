class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1 if x > 0 else -1

        temp = int(str(x * sign)[::-1])

        if sign == 1 and temp > 2**31 - 1:
            return 0

        if sign == -1 and temp > 2**31:
            return 0

        return sign * temp

s = Solution()
print s.reverse(123)
print s.reverse(1234357345)
print s.reverse(0)
print s.reverse(-123)
print s.reverse(1200)
print s.reverse(-12300)