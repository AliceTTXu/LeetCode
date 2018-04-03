import itertools
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        digits = [int(time[i]) for i in range(5) if i != 2]
        initial_mins = self.calculate_abs_mins(digits)
        max_mins = 24 * 60
        temp_min_gap, closets_time = max_mins, None
        for candidate in itertools.product(digits, repeat = 4):
            if not self.is_valid_time(candidate):
                continue
            abs_mins = self.calculate_abs_mins(candidate)
            temp_gap = (abs_mins - initial_mins) % max_mins
            if temp_gap > 0 and temp_gap < temp_min_gap:
                temp_min_gap, closets_time = temp_gap, candidate

        return '{}{}:{}{}'.format(*closets_time) if closets_time else time

    def is_valid_time(self, time):
        return time[0] * 10 + time[1] < 24 and time[2] * 10 + time[3] < 60

    def calculate_abs_mins(self, time):
        return (time[0] * 10 + time[1]) * 60 + time[2] * 10 + time[3]

    def permutation(self, nums):
        if len(nums) == 1:
            return [nums]

        out = []

        for i in range(len(nums)):
            out += [[nums[i]] + x for x in self.permutation(nums[: i] + nums[i + 1:])]

        return out

s = Solution()
print s.nextClosestTime("00:00")
# print s.permutation([1,2,3,4])