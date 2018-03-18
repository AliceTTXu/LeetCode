class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        result = []

        def combinationSumCore(target, out):
            if not target:
                result.append(out)
                return
            for x in candidates:
                if x > target:
                    break
                if out and x < out[-1]:
                    continue
                else:
                    combinationSumCore(target - x, out + [x])

        combinationSumCore(target, [])

        return result

