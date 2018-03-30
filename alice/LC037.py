class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.board = board
        self.solve()

    def solve(self):
        coord = find_unfilled()
        if coord == (-1, -1):
            return True
        for x in xrange(9):
            if is_valid_in_row(coord[0], x) and is_valid_in_col(coord[1], x) and is_valid_in_square(coord[0], coord[1], x):
                self.board[coord[0]][coord[1]] = x
                if self.solve():
                    return True
                else:
                    self.board[coord[0]][coord[1]] = '.'
        return False

    def find_unfilled(self):
        for i in xrange(9):
            for j in xrange(9):
                if self.board[i][j] == '.':
                    return (i, j)
        return (-1, -1)

    def is_valid_in_row(self, row, num):
        for i in xrange(9):
            if self.borad[row][i] == num:
                return False
        return True

    def is_valid_in_col(self, col, num):
        for i in xrange(9):
            if self.board[i][col] == num:
                return False
        return True

    def is_valid_in_square(self, row, col, num):
        row0 = row / 3
        col0 = col / 3
        for i in xrange(3):
            for j in xrange(3):
                if self.board[row0 + i][col0 + j] == num:
                    return False
        return True