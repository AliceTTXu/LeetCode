class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # if n <= 0:
        #     return ''

        out = '1'

        for i in xrange(n - 1):
            tempOut = ''
            current = None
            count = 0
            for x in out:
                if not current:
                    current = x
                    count = 1
                elif current == x:
                    count += 1
                else:
                    tempOut += str(count) + current
                    current = x
                    count = 1
            out = tempOut + str(count) + current

        return out

s = Solution()
print s.