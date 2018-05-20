import heapq

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        intervals.sort(key = lambda x: x.start)
        n_room = 0
        endings = []

        for interval in intervals:
            while endings and endings[0] <= interval.start:
                    heapq.heappop(endings)

            heapq.heappush(endings, interval.end)
            n_room = max(n_room, len(endings))

        return n_room
