class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]

        unique = set()
        out = []
        for i in xrange(len(nums)):
            if nums[i] not in unique:
                unique.add(nums[i])
                out += [[nums[i]] + x for x in self.permuteUnique(nums[:i] + nums[i + 1:])]
        return out

        
s = Solution()
print s.permuteUnique([1,1,2])