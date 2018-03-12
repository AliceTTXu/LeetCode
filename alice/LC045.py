class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0

        left = right = 0
        step = 0

        while right < len(nums) - 1:
            step += 1
            far_most = right
            for i in xrange(left, right + 1):
                if i + nums[i] > far_most:
                    far_most = i + nums[i]
            left = right + 1
            right = far_most

        return step
