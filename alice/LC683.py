class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        
        candidates = []
        day = [0 for i in range(len(flowers))]
        for i, x in enumerate(flowers):
            day[x - 1] = i

        l, r = 0, k + 1

        while r < len(flowers):
            for i in xrange(l + 1, r):
                if day[i] < day[l] or day[i] < day[r]:
                    l, r = i, i + k + 1
                    break
            else:
                candidates.append(max(day[l], day[r]))
                l, r = r, r + k + 1

        return min(candidates) if candidates else -1