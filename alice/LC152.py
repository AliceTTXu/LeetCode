class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return
        
        out = nums[0]        
        curr_min = nums[0]
        curr_max = nums[0]
        
        for x in nums[1:]:
            if x < 0:
                curr_min, curr_max = min(x, curr_max * x), max(x, curr_min * x)
            else:
                curr_min = min(x, curr_min * x)
                curr_max = max(x, curr_max * x)
            out = max(out, curr_max)
        
        return out