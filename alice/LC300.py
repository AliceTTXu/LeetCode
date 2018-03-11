class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        dp = []
        currentMax = ()

        for i, x in enumerate(nums):
            if i == 0:
                dp.append([(1, x), (0, -float("inf"))])
                currentMax = (1, x)
            else:
                temp1 = temp2 = 0
                for y in dp:
                    if x > y[0][1] and y[0][0] + 1 > temp1:
                        temp1 = y[0][0] + 1
                    if x > y[1][1] and y[1][0] + 1 > temp2:
                        temp2 = y[1][0] + 1
                if temp1 > temp2:
                    dp.append([(temp1, x), currentMax])
                else:
                    dp.append([(temp2, x), currentMax])
                if max(temp1, temp2) > currentMax[0]:
                    currentMax = (max(temp1, temp2), x)
                elif max(temp1, temp2) == currentMax[0]:
                    currentMax = (max(temp1, temp2), min(x, currentMax[1]))

        return dp

    def lengthOfLIS1(self, nums):
        
        if not nums:
            return 0

        dp = [1 for x in nums]
        currentMax = 1

        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                if nums[j] > nums[i] and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                if dp[j] > currentMax:
                    currentMax = dp[j]

        return currentMax

s = Solution()
print s.lengthOfLIS1([10,9,2,5,3,7,101,18])
print s.lengthOfLIS1([1,2,3,4,5])
print s.lengthOfLIS1([5,4,3,2,1])
print s.lengthOfLIS1([3,5,6,2,5,4,19,5,6,7,12])