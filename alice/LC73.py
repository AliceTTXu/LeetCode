class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        orig = [False, False]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        orig[0] = True
                    if j == 0:
                        orig[1] = True

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0

        if orig[0]:
            matrix[0] = [0] * n
        if orig[1]:
            for j in range(m):
                matrix[j][0] = 0