class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        if not matrix:
            return

        self.row = len(matrix)
        self.col = len(matrix[0])
        self.matrix = [[0] * self.col for _ in range(self.row)]
        for i in xrange(self.row):
            for j in xrange(self.col):
                self.matrix[i][j] = self.matrix[max(0, i - 1)][j] + matrix[i][j]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """

        origin = self.matrix[0][col] if not row else self.matrix[row][col] - self.matrix[row - 1][col]
        for i in range(row, self.row):
            self.matrix[i][col] += (val - origin)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        bottom = sum([self.matrix[row2][j] for j in range(col1, col2 + 1)])
        top = 0 if not row1 else sum([self.matrix[row1 - 1][j] for j in range(col1, col2 + 1)])

        return bottom - top


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)