# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        out = []

        axis = []
        for i, x in enumerate(intervals):
            axis.extend([(x.start, i), (x.end, i)])

        axis.sort()

        one_interval_set = set([])
        one_interval_start = one_interval_end = None

        for x in axis:
            if x[1] not in one_interval_set:
                one_interval_set.add(x[1])
                if len(one_interval_set) == 1:
                    if x[0] == one_interval_end:
                        continue
                    else:
                        if one_interval_start is not None:
                            out.append(Interval(one_interval_start, one_interval_end))
                        one_interval_start = x[0]
            else:
                one_interval_set.remove(x[1])
                if len(one_interval_set) == 0:
                    one_interval_end = x[0]

        if one_interval_start is not None:
            out.append(Interval(one_interval_start, one_interval_end))

        return out