class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0

        row_repeat = 0
        col_repeat = 0
        m = len(grid)
        n = len(grid[0])

        for i in xrange(1, m):
            row_repeat += sum([grid[i][j] & grid[i - 1][j] for j in range(n)])

        for i in xrange(1, n):
            col_repeat += sum([grid[j][i] & grid[j][i - 1] for j in range(m)])

        return sum([sum(x) for x in grid]) * 4 - 2 * (row_repeat + col_repeat)