class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        curr_max = 0
        out = 0

        for i, x in enumerate(arr):
            curr_max = max(x, curr_max)
            if curr_max == i:
                out += 1

        return out