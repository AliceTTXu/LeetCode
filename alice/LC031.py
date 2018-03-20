class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        first_turn = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                first_turn = i - 1
                break

        print first_turn

        if first_turn is None:
            nums.sort()
            return

        next_bigger = None
        for i in range(len(nums) - 1, first_turn, -1):
            if nums[i] > nums[first_turn]:
                next_bigger = i
                break

        nums[first_turn], nums[next_bigger] = nums[next_bigger], nums[first_turn]

        print range((len(nums) - first_turn - 1) / 2)

        for i in range((len(nums) - first_turn - 1) / 2):
            nums[first_turn + 1 + i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[first_turn + 1 + i]

        return nums

s = Solution()
print s.nextPermutation([1, 3, 2])