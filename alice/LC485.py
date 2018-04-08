class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        out = temp = 0
        pre = 0

        for x in nums:
            if x:
                temp += 1
                out = max(out, temp)
            else:
                temp = 0

        return out