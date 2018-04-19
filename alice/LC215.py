class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        index = self.partition(nums, 0, len(nums) - 1)

        if len(nums) - index > k:
            return self.findKthLargest(nums[index + 1:], k)
        elif len(nums) - index < k:
            return self.findKthLargest(nums[:index], k - (len(nums) - index))
        else:
            return nums[index]
        
    def partition(self, nums, l, r):
        pivot = nums[-1]
        index = l
        for i in xrange(len(nums)):
            if nums[i] < pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[-1] = nums[-1], nums[index]
        return index

s = Solution()
# print s.findKthLargest([3,2,1,5,6,4], 5)
# print s.findKthLargest([2,2], 1)
print s.partition([2,2], 0,1)
# print s.partition([3,2,1,5,6,4], 0, 5)