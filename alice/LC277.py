# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        candidate = 0
        for i in xrange(n):
            if knows(candidate, i):
                candidate = i

        for i in xrange(candidate):
            if knows(candidate, i):
                return -1
        for i in xrange(candidate + 1, n):
            if not knows(i, candidate):
                return -1
        
        return candidate

    def findCelebrity_slow(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        candidates = [True] * n
        count = 0
        for i in xrange(n):
            for j in xrange(n):
                if i != j and candidates[j]:
                    if not knows(i, j) or (knows(i, j) and knows(j, i)):
                        candidates[j] = False
                        count += 1
            if count == n:
                return -1

        return candidates.index(True)