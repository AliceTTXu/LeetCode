import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        self.counts = collections.Counter(nums)
        out = []

        while len(out) < k:
            # print out
            self.pivot(out, k - len(out))

        return out

    def pivot(self, out, n):
        pivot = None
        tt = None
        left = {}
        right = {}

        for x in self.counts:
            if pivot is None:
                pivot = self.counts[x]
                tt = x
                continue
            if self.counts[x] >= pivot:
                right[x] = self.counts[x]
            elif self.counts[x] < pivot:
                left[x] = self.counts[x]
        # print pivot, left, right
        if len(right) == n:
            out.extend(right.keys())
        elif len(right) < n:
            out.extend(right.keys() + [tt])
            self.counts = left
        else:
            self.counts = right

s = Solution()
print s.topKFrequent([4,1,-1,2,-1,2,3], 2)
print s.topKFrequent([1,2], 2)