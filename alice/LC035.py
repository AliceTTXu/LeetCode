class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        out = 0

        for i in xrange(len(nums)):
            if nums[i] >= target:
                out = i
                break
            elif i == len(nums) - 1:
                out = i + 1

        return out

s = Solution()
print s.searchInsert([1, 3, 5, 6], 5)
print s.searchInsert([1, 3, 5, 6], 2)
print s.searchInsert([1, 3, 5, 6], 7)
print s.searchInsert([1, 3, 5, 6], 0)
print s.searchInsert([], 5)