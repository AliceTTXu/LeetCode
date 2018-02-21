class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)
        
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                nums.pop(i)

        return len(nums)

s = Solution()
print s.removeDuplicates([1, 1, 2])
print s.removeDuplicates([])
print s.removeDuplicates([1])
print s.removeDuplicates([1, 2, 3])
print s.removeDuplicates([1, 1, 1])