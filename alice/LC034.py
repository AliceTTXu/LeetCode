class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = 0, len(nums) - 1
        leftOut = -1

        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid == 0:
                    leftOut = 0
                    break
                elif nums[mid - 1] != target:
                    leftOut = mid
                    break
                else:
                    right = mid - 1

        if leftOut == -1:
            return [-1, -1]

        left, right = leftOut, len(nums) - 1

        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid == len(nums) - 1:
                    rightOut = len(nums) - 1
                    break
                elif nums[mid + 1] != target:
                    rightOut = mid
                    break
                else:
                    left = mid + 1

        return [leftOut, rightOut]



s = Solution()
print s.searchRange([1,2,2,2,2,3,4,5], 3)
print s.searchRange([], 3)
print s.searchRange([1,2,2,2,2,3,4,5], 6)
print s.searchRange([1,2,2,2,2,3,4,5], 0)
print s.searchRange([1,2,2,2,2,3,4,5], 2)
print s.searchRange([1,2,2,2,2,3,4,5,6,7,8,9,10], 7)
print s.searchRange([1,2,2,2,2,3,4,5,6,7,8,9,10], 2)
