class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for x in board:
            temp = [num for num in x if num != '.']
            if len(set(temp)) != len(temp):
                return False

        for x in zip(*board):
            temp = [num for num in x if num != '.']
            if len(set(temp)) != len(temp):
                return False

        for i in range(3):
            for j in range(3):
                tempAll = []
                tempAll += [board[i * 3 + l][j * 3 + k] for k in range(3) for l in range(3)]
                temp = [num for num in tempAll if num != '.']
                if len(set(temp)) != len(temp):
                    return False

        return True


s = Solution()
print s.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]])