class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        temp = ''
        for x in num:
            if x in mapping:
                temp += mapping[x]
            else:
                return False

        return num == temp[::-1]