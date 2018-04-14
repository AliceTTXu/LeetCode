class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        current = []
        out = []

        for x in nums:
            if len(current) == 0:
                current. append(x)
            elif len(current) == 1:
                if x == current[0] + 1:
                    current.append(x)
                else:
                    out.append((current[0]))
                    current = [x]
            else:
                if x == current[-1] + 1:
                    current[-1] = x
                else:
                    out.append(str(current[0]) + '->' + str(current[1]))
                    current = [x]

        if len(current) == 1:
            out.append(str(current[0]))
        elif len(current) == 2:
            out.append(str(current[0]) + '->' + str(current[1]))

        return out