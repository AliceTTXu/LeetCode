class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        row_direction = self.process_one_direction(board)
        if row_direction == -1:
            return -1
        col_direction = self.process_one_direction(zip(*board))
        if col_direction == -1:
            return -1
        
        return row_direction + col_direction

    def process_one_direction(self, board):
        distinct_lines = set(map(tuple, board))
        if len(distinct_lines) != 2:
            return -1

        N = len(board)
        line1, line2 = tuple(distinct_lines)

        if sorted([sum(line1), sum(line2)]) != [N / 2, (N + 1) / 2]:
            return -1

        if not all([x ^ y for x, y in zip(line1, line2)]):
            return -1

        template = [1, 0] * (N / 2) + [1] * (N % 2)
        
        if N % 2 == 1:
            if sum(line1) == N / 2:
                out = sum([x ^ y for x, y in zip(line2, template)]) / 2
            else:
                out = sum([x ^ y for x, y in zip(line1, template)]) / 2
        else:
            out = min(sum([x ^ y for x, y in zip(line1, template)]), sum([x ^ (y ^ 1) for x, y in zip(line1, template)])) / 2

        return out