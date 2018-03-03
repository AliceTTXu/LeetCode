class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [nums]

        out = []

        for i in xrange(len(nums)):
            out += [[nums[i]] + y for y in self.permute(nums[:i] + nums[i + 1:])]
            
        return out

s = Solution()
print s.permute([1,2,3])