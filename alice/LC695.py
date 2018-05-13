class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0
        
        seen = set()
        max_area = 0

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    stack = [(i, j)]
                    temp_area = 0
                    while stack:
                        point = stack.pop()
                        if point not in seen:
                            seen.add(point)
                            temp_area += 1
                            ii, jj = point
                            neighbours = [(max(0, ii - 1), jj), (min(len(grid) - 1, ii + 1), jj), (ii, max(0, jj - 1)), (ii, min(len(grid[0]) - 1, jj + 1))]
                            stack.extend([x for x in neighbours if grid[x[0]][x[1]] == 1 and x not in seen])
                    max_area = max(max_area, temp_area)

        return max_area