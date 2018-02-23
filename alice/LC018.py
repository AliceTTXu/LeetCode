class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        out = []
        self.NSum(nums, target, 4, [], out)
        return out


    def NSum(self, nums, target, N, result, output):
    	if len(nums) < N or N < 2:
    		return
    	if N == 2:
    		i = 0
    		j = len(nums) - 1
    		while i < j:
    			if nums[i] + nums[j] == target:
    				output.append(result + [nums[i], nums[j]])
    				while i < j and nums[i + 1] == nums[i]:
    					i += 1
    				while j < i and nums[j - 1] == nums[j]:
    					j -= 1
    				i += 1
    				j -= 1
    			elif nums[i] + nums[j] < target:
    				i += 1
    			else:
    				j -= 1
    	else:
    		for index in xrange(len(nums) - N + 1):
    			if index == 0 or nums[index] != nums[index - 1]:
    				self.NSum(nums[index + 1:], target - nums[index], N - 1, result + [nums[index]], output)

s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)

# print s.NSum([-2, -1, -1, 0, 2], 0, 2, [], [])


