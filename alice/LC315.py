class BinaryIndexedTree(object):

    def __init__(self, n):
        self.counts = [0] * (n + 1)

    def update(self, i):
        while i < len(self.counts):
            self.counts[i] += 1
            i += (i & (-i))

    def sum(self, i):
        out = 0
        while i > 0:           
            out += self.counts[i]
            i -= (i & (-i))
        return out

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ordering = {x: i for i, x in enumerate(sorted(set(nums)), 1)}
        tree = BinaryIndexedTree(len(ordering))
        result = []

        for num in nums[::-1]:
            result.append(tree.sum(ordering[num] - 1))
            tree.update(ordering[num])

        return result[::-1]