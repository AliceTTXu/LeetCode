class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counts = {}
        interval = {}
        min_interval = 0
        max_count = 0
        
        for i, x in enumerate(nums):
            if x not in counts:
                counts[x] = 1
                interval[x] = (i, i)
            else:
                counts[x] += 1
                interval[x] = (interval[x][0], i)
            if counts[x] > max_count:
                max_count = counts[x]
                min_interval = interval[x][1] - interval[x][0] + 1
            elif counts[x] == max_count:
                min_interval = min(min_interval, interval[x][1] - interval[x][0] + 1)
                
        return min_interval