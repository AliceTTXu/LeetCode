class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0

        counts = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(counts)):
            temp = 0
            for j in range(len(counts[0])):
                if grid[i][j] == 'W':
                    temp = 0
                elif grid[i][j] == 'E':
                    temp += 1
                else:
                    counts[i][j] += temp
                    
            temp = 0            
            for j in range(len(counts[0]) - 1, -1, -1):
                if grid[i][j] == 'W':
                    temp = 0
                elif grid[i][j] == 'E':
                    temp += 1
                else:
                    counts[i][j] += temp
        
        for j in range(len(counts[0])):
            temp = 0
            for i in range(len(counts)):
                if grid[i][j] == 'W':
                    temp = 0
                elif grid[i][j] == 'E':
                    temp += 1
                else:
                    counts[i][j] += temp
            
            temp = 0
            for i in range(len(counts) - 1, -1, -1):
                if grid[i][j] == 'W':
                    temp = 0
                elif grid[i][j] == 'E':
                    temp += 1
                else:
                    counts[i][j] += temp

        return max([max(x) for x in counts])LC