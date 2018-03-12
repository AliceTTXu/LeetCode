class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if x == 0.0:
            return 0.0
        else:
            if n == 0:
                return 1.0
            elif n > 0:
                return self.binary_multiply(x, n)
            else:
                return 1 / self.binary_multiply(x, -n)

    def binary_multiply(self, x, n):
        if n == 0:
            return 1.0
        print n
        half_length = n / 2
        half_result = self.binary_multiply(x, half_length)
        if half_length * 2 == n:
            return half_result * half_result
        else:
            return half_result * half_result * x

s = Solution()
# print s.myPow(1, 10)
# print s.myPow(1.1, 10)
# print s.myPow(1.1, -10)
# print s.myPow(1.1, 1)
# print s.myPow(-1.1, 3)
# print s.myPow(-1.1, 4)
# print s.myPow(1, 0)
# print s.myPow(0, 10)
print s.myPow(0.00001, 2147483647)
# print s.binary_multiply(2, 0)