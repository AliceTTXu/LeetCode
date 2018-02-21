import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x < 10:
            return True

        length = int(math.floor(math.log(abs(x), 10)) + 1)
        halfLength = length / 2

        if x / 10**(length - halfLength) == sum([((x % 10**(i + 1)) / 10**i) * 10**(halfLength - i - 1) for i in xrange(halfLength)]):
            return True
        else:
            return False


s = Solution()
print s.isPalindrome(12321)
print s.isPalindrome(0)
print s.isPalindrome(11)
print s.isPalindrome(123321)
print s.isPalindrome(123545)