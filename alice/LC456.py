class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3:
            return False
        
        sofar_min = []
        temp = nums[0]
        for x in nums:
            temp = min(temp, x)
            sofar_min.append(temp)

        stack = []
        for i in xrange(len(nums) - 1, -1, -1):
            if nums[i] > sofar_min[i]:
                while stack and stack[-1] <= sofar_min[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])

        return False

