class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return
        
        self.board = board
        self.m = len(board)
        self.n = len(board[0])

        for i in xrange(self.m):
            for j in xrange(self.n):
                nb = self.count_neighbours(i, j)
                if self.board[i][j] == 1 and (nb < 2 or nb > 3):
                    self.board[i][j] = 3
                elif self.board[i][j] == 0 and nb == 3:
                    self.board[i][j] = 2

        for i in xrange(self.m):
            for j in xrange(self.n):
                if self.board[i][j] == 3:
                    self.board[i][j] = 0
                elif self.board[i][j] == 2:
                    self.board[i][j] = 1

    def count_neighbours(self, x, y):
        tot = 0
        for i in range(max(0, x - 1), min(self.m, x + 2)):
            for j in range(max(0, y - 1), min(self.n, y + 2)):
                tot += self.board[i][j] % 2

        return tot - self.board[x][y]