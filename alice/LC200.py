class Solution(object):
    def numIslands_UnionFind_WithBug(self, grid):

        if not grid or not grid[0]:
            return 0

        self.parent = []
        self.rank = []
        m = len(grid)
        n = len(grid[0])
        self.out = 0

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    self.parent.append(i * m + j)
                    self.rank.append(1)
                    self.out += 1
                else:
                    self.parent.append(0)
                    self.rank.append(0)

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if i > 0 and grid[i - 1][j] == '1':
                        self.UF_union(i * m + j, (i - 1) * m + j)
                    if i < m - 1 and grid[i + 1][j] == '1':
                        self.UF_union(i * m + j, (i + 1) * m + j)
                    if j > 0 and grid[i][j - 1] == '1':
                        self.UF_union(i * m + j, i * m + j - 1)
                    if j < n - 1 and grid[i][j + 1] == '1':
                        self.UF_union(i * m + j, i * m + j + 1)

        return self.out

    def UF_union(self, index1, index2):
        p1 = self.UF_find(index1)
        p2 = self.UF_find(index2)

        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p1] = p2
                self.rank[p2] += 1
            self.out -= 1

    def UF_find(self, index):
        if index != self.parent[index]:
            self.parent[index] = self.UF_find(self.parent[index])
        return self.parent[index]



    def numIslands_DFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        n_island = 0
        
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    n_island += 1
                    stack = [(i, j)]
                    while stack:
                        center = stack.pop()
                        if grid[max(center[0] - 1, 0)][center[1]] == '1':
                            grid[max(center[0] - 1, 0)][center[1]] = '0'
                            stack.append((max(center[0] - 1, 0), center[1]))
                        if grid[min(center[0] + 1, len(grid) - 1)][center[1]] == '1':
                            grid[min(center[0] + 1, len(grid) - 1)][center[1]] = '0'
                            stack.append((min(center[0] + 1, len(grid)), center[1]))
                        if grid[center[0]][max(center[1] - 1, 0)] == '1':
                            grid[center[0]][max(center[1] - 1, 0)] = '0'
                            stack.append((center[0], max(center[1] - 1, 0)))
                        if grid[center[0]][min(center[1] + 1, len(grid[0]) - 1)] == '1':
                            grid[center[0]][min(center[1] + 1, len(grid[0]) - 1)] = '0'
                            stack.append((center[0], min(center[1] + 1, len(grid[0]))))

        return n_island

s = Solution()
print s.numIslands([["1","1","1"],["0","1","0"],["0","1","0"]])