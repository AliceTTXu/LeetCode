class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) / 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

s = Solution()
print s.search([4,5,6,7,0,1,2], 1)
print s.search([4,5,6,7,0,1,2], 0)
print s.search([4,5,6,7,0,1,2], 5)
print s.search([4,5,6,7,0,1,2], 4)
print s.search([4,5,6,7,0,1,2], 7)
print s.search([0,1,2,3,4,5,6], 4)
print s.search([], 1)
print s.search([0,1,2,3,4,5,6], 9)