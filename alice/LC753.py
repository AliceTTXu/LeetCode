import random
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        seen = set(['0' * n])
        out = '0' * n

        def DFS(out):
            if len(out) == k**n + n - 1:
                return out 
            for i in range(k):
                candidate = out[len(out) - n + 1:] + str(i)
                if candidate not in seen:
                    seen.add(candidate)
                    temp = DFS(out + str(i))
                    if temp and len(temp) == k**n + n - 1:
                        return temp
                    else:
                        seen.remove(candidate)

        return DFS(out)

s = Solution()
print s.crackSafe1(4, 4)