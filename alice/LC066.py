class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        forward = 1

        for i in reversed(range(len(digits))):
            temp = digits[i] + forward
            digits[i] = temp % 10
            forward = temp / 10

        if forward:
            digits.insert(0, 1)

        return digits