class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        out = [0, 1]

        while len(out) < num + 1:
            out.extend([x + 1 for x in out])

        return out[: num + 1]