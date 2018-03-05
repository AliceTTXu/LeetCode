class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if not n:
            return ['']
        else:
            return self.generateParenthesisCore(n - 1, 1, ['('])

    def generateParenthesisCore(self, n, leftCount, out):
        if n > 0:
            if leftCount > 0:
                part1 = self.generateParenthesisCore(n, leftCount - 1, [x + ')' for x in out])
            else:
                part1 = []
            part2 = self.generateParenthesisCore(n - 1, leftCount + 1, [x + '(' for x in out])
            return part1 + part2
        else:
            if leftCount > 0:
                return [x + ')' * leftCount for x in out]

    def generateParenthesis2(self, n):
        if not n:
            return ['']
        out = []
        for i in xrange(n):
            for left in self.generateParenthesis2(i):
                for right in self.generateParenthesis2(n - i - 1):
                    out.append('({}){}'.format(left, right))
        return out

s = Solution()
print s.generateParenthesis2(3)