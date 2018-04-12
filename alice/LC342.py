class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        bin_str = bin(num)
        
        return num == 1 or (bin_str[2] == '1' and int(bin_str[3:]) == 0 and len(bin_str[3:]) % 2 == 0)