class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        out = len(nums)
        
        for i in xrange(len(nums)):
            current = nums[i]

            while current > 0 and current <= out:
                if current != nums[current - 1]:
                    temp = nums[current - 1]
                    nums[current - 1] = current
                    current = temp
                else:
                    break

        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return out + 1

s = Solution()
print s.firstMissingPositive([0,-1,-3,-5,1])