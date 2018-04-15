class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        out = []
        for x in nums:
            index = abs(x) - 1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                out.append(index + 1)
        
        return out