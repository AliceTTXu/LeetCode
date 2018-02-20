class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        rule = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}

        lefts = []

        for x in list(s):
            if rule[x] > 0:
                lefts.append(rule[x])
            else:
                try:
                    if lefts[-1] + rule[x] == 0:
                        lefts.pop()
                    else:
                        return False
                except IndexError:
                    return False

        if lefts == []:
            return True
        else:
            return False


s = Solution()
print s.isValid('((({{[{()}]}})))')
print s.isValid('')
print s.isValid('[]{}')
print s.isValid('(({{[]([]{})}}))')
print s.isValid('(([])')
print s.isValid('(]')
print s.isValid(']]]')