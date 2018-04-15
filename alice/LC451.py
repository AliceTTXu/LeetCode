import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        counts = collections.Counter(s)
        temp = [''] * len(s)

        for x in counts:
            temp[~(counts[x] - 1)] += x * counts[x]

        return ''.join(temp)