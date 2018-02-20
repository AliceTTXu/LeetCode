class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if nums == []:
            return nums

        if type(nums[0]) is int:
            return self.subsets([[nums]])

        last = nums.pop()

        if len(last[0]) == 1:
            nums.extend(last)
            nums.append([])
            return nums
        else:
            nums.extend(last)
            nums.append(self.removeOneElement(last))
            return self.subsets(nums)

    def removeOneElement(self, li):
        nest = [[x[0:i] + x[i + 1:] for i in range(len(x))] for x in li]
        flatten = set([tuple(x) for sublist in nest for x in sublist])
        return [list(x) for x in flatten]

    def subsets2(self, nums):
        bins = [bin(x)[2:].zfill(len(nums)) for x in range(2**len(nums))]
        return [self.oneSubset(x, nums) for x in bins]
        
    def oneSubset(self, binRule, originalList):
        out = []
        for i in range(len(originalList)):
            if binRule[i] == '1':
                out.append(originalList[i])
        return out


s = Solution()
print s.subsets2([])
print s.subsets2([1])
print s.subsets2([1, 2, 3])
