class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for x in nums:
            while nums[x - 1] != x:
                temp = nums[x - 1]
                nums[x - 1] = x
                x = temp

        out = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                out.append(i + 1)

        return out