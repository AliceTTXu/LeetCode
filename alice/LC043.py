class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if not num1 or not num2:
            return

        temp = [0 for x in range(len(num1) + len(num2))]
        
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                one_step = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                temp[i + j] += one_step / 10
                temp[i + j + 1] += one_step % 10

        out_N = 0
        for i in xrange(len(temp)):
            out_N += temp[i] * 10**(len(temp) - i - 1)

        return str(out_N)

s = Solution()
print s.multiply("", "")
