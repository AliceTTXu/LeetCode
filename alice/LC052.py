class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        self.result = 0
        self.N = n

        self.DFS(set(), set(), set())

        return self.result

    def DFS(self, queens, sums, diffs):
        if len(queens) == self.N:
            self.result += 1
        else:
            row = len(queens)
            for col in xrange(self.N):
                if col not in queens and (row + col) not in sums and (row - col) not in diffs:
                    queens.add(col)
                    sums.add(row + col)
                    diffs.add(row - col)
                    self.DFS(queens, sums, diffs)
                    queens.remove(col)
                    sums.remove(row + col)
                    diffs.remove(row - col)
