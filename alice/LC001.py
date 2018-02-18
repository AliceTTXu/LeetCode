class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(i, x) for i, x in enumerate(nums)]
        nums.sort(key = lambda num: num[1])
        leftP = 0
        rightP = len(nums) - 1
        while True:
            if nums[leftP][1] + nums[rightP][1] > target:
                rightP -= 1
            elif nums[leftP][1] + nums[rightP][1] < target:
                leftP += 1
            else:
                return [nums[leftP][0], nums[rightP][0]]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}
        for i, x in enumerate(nums):
            if target - x in mem:
                return [i, mem[target - x]]
            mem[x] = i


s = Solution()
print s.twoSum2([8, 2, 7, 11, 15], 9)
print s.twoSum2([-3, 0, 7, -5, 2], 4)
print s.twoSum2([2, 1], 3)