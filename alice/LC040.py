class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        result = []

        def combinationSum2Core(target, out, index):
            if not target:
                result.append(out)
                return
            i = index
            while i < len(candidates):
                if candidates[i] > target:
                    return
                else:
                    combinationSum2Core(target - candidates[i], out + [candidates[i]], i + 1)
                i += 1

        combinationSum2Core(target, [], 0)

        return result