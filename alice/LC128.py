class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = set(nums)
        out = 0
        
        for x in nums:
            if x - 1 not in nums:
                temp = 1
                curr = x
                while curr + 1 in nums:
                    curr += 1
                    temp += 1
                out = max(out, temp)
                
        return out
                    