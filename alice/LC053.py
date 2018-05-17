class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        out = nums[0]
        temp = nums[0]

        for num in nums[1:]:
            temp = max(temp + num, num)
            out = max(out, temp)

        return out

    


