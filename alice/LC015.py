class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        out = []
        
        if len(nums) < 3:
            return out

        nums.sort()

        for i in xrange(len(nums[:-2])):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while k > j:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif temp > 0:
                    k -= 1
                else:
                    j += 1

        return out

s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, 4])