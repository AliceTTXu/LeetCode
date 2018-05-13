class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) / 2
            if mid % 2 == 0:
                move = 1
            else:
                move = -1
            if nums[mid] == nums[mid + move]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]