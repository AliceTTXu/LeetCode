class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        pre1 = nums[0]
        pre2 = max(nums[0:2])

        for x in nums[2:]:
            pre1, pre2 = pre2, max(pre1 + x, pre2)

        return pre2