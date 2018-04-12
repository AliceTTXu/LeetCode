class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        bin_str = bin(n)
        
        return n == 1 or (bin_str[2] == '1' and int(bin_str[3:]) == 0)