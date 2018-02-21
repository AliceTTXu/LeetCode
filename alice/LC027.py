class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in xrange(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)

        return len(nums)

    def removeElement2(self, nums, val):
        flag = True
        while flag:
            try:
                nums.remove(val)
            except ValueError:
                flag = False
        return len(nums)

s = Solution()
print s.removeElement2([3, 2, 2, 3], 3)
print s.removeElement2([], 3)
print s.removeElement2([1,2,1,2,1], 3)