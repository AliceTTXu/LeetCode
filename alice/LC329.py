class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]:
            return 0

        self.N = len(matrix)
        self.M = len(matrix[0])
        self.matrix = matrix
        max_path = 0
        self.cache = [[0 for _ in range(self.M)] for _ in range(self.N)]

        for i in xrange(self.N):
            for j in xrange(self.M):
                max_path = max(max_path, self.DFS(i, j))

        return max_path

    def DFS(self, i, j):
        if self.cache[i][j] != 0:
            return self.cache[i][j]

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        stack = [(i, j)]
        temp_max = 1

        while stack:
            current_pos = stack.pop()
            for move in moves:
                x = current_pos[0] + move[0]
                y = current_pos[1] + move[1]
                if 0 <= x < self.N and 0 <= y < self.M and self.matrix[x][y] > self.matrix[i][j]:
                    temp_max = max(temp_max, self.DFS(x, y) + 1)

        self.cache[i][j] = temp_max

        return self.cache[i][j]