class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        row, col = len(matrix), len(matrix[0])
        for i in xrange(row):
            matrix[i] = [-1] * (row - i - 1) + matrix[i] + [-1] * i

        for x in zip(*matrix):
            temp = set(x)
            temp.discard(-1)
            if len(temp) != 1:
                return False

        return True