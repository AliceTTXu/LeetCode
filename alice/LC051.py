class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        self.queens = []
        self.N = n

        self.DFS([], [], [])
        out = []

        for queen in self.queens:
            temp = []
            for j in queen:
                temp += ['.' * j + 'Q' + '.' * (n - j - 1)]
            out.append(temp)
        return out

    def DFS(self, queens, sums, diffs):
        if len(queens) == self.N:
            self.queens.append(queens)
        else:
            row = len(queens)
            for col in xrange(self.N):
                if col not in queens and (row + col) not in sums and (row - col) not in diffs:
                    self.DFS(queens + [col], sums + [row + col], diffs + [row - col])
