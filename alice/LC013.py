from functools import reduce

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = [mapping[x] for x in list(s)]
        sign = map((lambda x, y: 1 if x >= y else -1), s[:len(s) - 1], s[1:])
        return sum([x * y for (x, y) in zip(s, sign)]) + s[-1]
        

s = Solution()
print s.romanToInt("CXCIX")
print s.romanToInt("I")
print s.romanToInt("MCDXXXVII")
print s.romanToInt("XCIX")
print s.romanToInt("MMMCMXCIX")


# def myFunc(tt):
# 	tt.append(1)
# 	return tt

# def myFunc2(tt):
# 	tt = [1, 2, 3]
# 	return tt

# qq = [3]
# myFunc(qq)
# print qq
# myFunc2(qq)
# print qq