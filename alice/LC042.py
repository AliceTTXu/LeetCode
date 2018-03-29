class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_height_left, max_height_right = [], []
        max_left = max_right = 0

        for x in height:
            max_left = max(max_left, x)
            max_height_left.append(max_left)

        for x in height[::-1]:
            max_right = max(max_right, x)
            max_height_right.append(max_right)

        out = 0

        for x in zip(height, max_height_left, max_height_right[::-1]):
            out += min(x[1], x[2]) - x[0]

        return out

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])