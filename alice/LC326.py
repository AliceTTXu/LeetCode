import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        temp = math.log(n, 3)
        print abs(temp - math.floor(temp)), abs(temp - math.ceil(temp))
        return min(abs(temp - math.floor(temp)), abs(temp - math.ceil(temp))) < 10**-10