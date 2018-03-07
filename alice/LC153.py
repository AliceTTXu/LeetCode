class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return
        
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) / 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

s = Solution()
print s.findMin([4,5,6,7,0,1,2])
print s.findMin([])
print s.findMin([0,1,2,4,5,6,7])
print s.findMin([4,5,6,7,0])
print s.findMin([4,0,1,2])