class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        flag = float("inf")
        out = 0

        for i in xrange(len(nums) - 2):
        	j = i + 1
        	k = len(nums) - 1
        	while j < k:
        		temp = nums[i] + nums[j] + nums[k]
        		if abs(target - temp) < flag:
        			flag = abs(target - temp)
        			out = temp
        		if flag == 0:
        			return out
        		if temp < target:
        			j += 1
        		else:
        			k -= 1

        return out

s = Solution()
print s.threeSumClosest([-1, 2, 1, -4], 1)