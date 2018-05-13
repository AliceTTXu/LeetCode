import collections, itertools

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        out = 0
        rows = [[i for i, x in enumerate(row) if x == 1] for row in grid]

        count = collections.Counter()

        for row in rows:
            for pair in itertools.combinations(row, 2):
                count[pair] += 1

        print count

