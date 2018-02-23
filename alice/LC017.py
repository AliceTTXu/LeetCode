class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []
        
        mapping = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': []
        }

        digitsList = [mapping[x] for x in digits]
        digitsCount = [len(x) for x in digitsList]
        for i in xrange(len(digitsCount) - 1):
            digitsCount[i + 1] *= digitsCount[i]
        
        out = []

        for i in xrange(len(digits)):
            if digits[i] == '1' or  digits[i] == '0':
                out.append(['' for j in range(digitsCount[-1])])
            else:
                out.append(list(''.join([x * (digitsCount[-1] / digitsCount[i]) for x in digitsList[i]] * (digitsCount[i] / len(digitsList[i])))))

        return [''.join([x[i] for x in out]) for i in xrange(digitsCount[-1])]

s = Solution()
print s.letterCombinations('0')