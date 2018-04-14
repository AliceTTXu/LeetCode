class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        out = []
        self.lower = lower
        self.upper = upper

        for x in nums:
            self.process_one(x, out)

        if self.lower == self.upper:
            out.append(str(self.lower))
        elif self.lower < self.upper:
            out.append(str(self.lower) + '->' + str(self.upper))

        return out

    def process_one(self, num, ranges):
        if num == self.lower:
            self.lower += 1     
        elif num == self.lower + 1:
            ranges.append(str(self.lower))
            self.lower += 2
        elif num > self.lower + 1:
            ranges.append(str(self.lower) + '->' + str(num - 1))
            self.lower = num + 1