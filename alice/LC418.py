class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """

        s = ' '.join(sentence) + ' '
        tot = 0
        sl = len(s)

        for i in xrange(rows):
            tot += cols
            while s[tot % sl] != ' ':
                tot -= 1
            tot += 1

        return tot / sl

    def wordsTyping_timeout(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
                
        dp = {}

        count = 0
        left = cols
        lines = 1

        while lines <= rows:
            if left not in dp:
                dp[left] = self.process_one(sentence, cols, left)

            if dp[left] == 'Failed':
                return 0

            (newlines, left) = dp[left]
            count += 1
            lines += newlines

        return count - 1

    def process_one(self, sentence, width, budget):
        lines = 0
        for x in sentence:
            if len(x) > width:
                return 'Failed'
            if len(x) <= budget:
                budget -= len(x) + 1
            else:
                lines += 1
                budget = width - len(x) - 1

        return lines, budget

s = Solution()
# print s.wordsTyping(["hello", "world"], 2, 8)
# print s.wordsTyping(["a", "bcd", "e"], 3, 6)
# print s.wordsTyping(["I", "had", "apple", "pie"], 4, 5)
print s.wordsTyping_timeout(["I"], 10000, 10000)