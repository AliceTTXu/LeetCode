import heapq, collections

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        lefts = [(b[0], b[2], 'l') for b in buildings]
        rights = [(b[1], b[2], 'r') for b in buildings]
        bonds = sorted(lefts + rights)
        self.heap = []
        result = []
        self.remove_counter = collections.Counter()
        self.remove_n = 0

        for x, h, b in bonds:
            if b == 'l':
                self.__remove()
                if not self.heap or h > -self.heap[0]:
                    if result and result[-1][0] == x and (result[-1][1] == 0 or result[-1][1] < h):
                        result[-1] = [x, h]
                    else:
                        result.append([x, h])
                heapq.heappush(self.heap, -h)
            else:
                self.remove_counter[-h] += 1
                self.remove_n += 1
                self.__remove()
                if not self.heap:
                    result.append([x, 0])
                elif h > -self.heap[0]:
                    if result and result[-1][0] == x and (result[-1][1] == 0 or result[-1][1] < h):
                        result[-1] = [x, h]
                    else:
                        result.append([x, -self.heap[0]])

        return result

    def __remove(self):
        if not self.heap:
            return
        while self.remove_n != 0 and self.remove_counter[self.heap[0]] != 0:
            self.remove_counter[self.heap[0]] -= 1
            self.remove_n -= 1
            heapq.heappop(self.heap)
