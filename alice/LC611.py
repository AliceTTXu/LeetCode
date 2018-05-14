class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 3:
            return 0

        nums.sort()
        out = 0

        for e1 in xrange(len(nums) - 2):
            if nums[e1] == 0:
                continue
            e3 = e1 + 2
            for e2 in xrange(e1 + 1, len(nums) - 1):
                while e3 < len(nums):
                    if nums[e1] + nums[e2] > nums[e3]:
                        e3 += 1
                out += e3 - e2 - 1

        return out