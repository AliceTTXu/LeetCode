class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        tempMax = 0

        i = 0
        j = len(height) - 1

        while i < j:
            print i, j
            tempMax = max(tempMax, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1

        return tempMax

s = Solution()
print s.maxArea([1, 1])