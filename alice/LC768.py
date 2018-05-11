class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        arr_sorted = sorted(arr)
        counting = {}
        out = 0
        flag = 0

        for x, y in zip(arr,arr_sorted):
            counting[x] = counting.get(x, 0) - 1

            if counting[x] == 0:
                flag -= 1
            if counting[x] == -1:
                flag += 1

            counting[y] = counting.get(y, 0) + 1
            
            if counting[y] == 0:
                flag -= 1
            if counting[y] == 1:
                flag += 1

            if flag == 0:
                out += 1

        return out

