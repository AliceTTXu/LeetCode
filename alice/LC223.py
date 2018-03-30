class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        total = (C - A) * (D - B) + (G - E) * (H - F)

        xs = [(A, 1), (C, 1), (E, 2), (G, 2)]
        ys = [(B, 1), (D, 1), (F, 2), (H, 2)]

        xs.sort()
        ys.sort()

        return total - self.find_overlap(xs) * self.find_overlap(ys)


    def find_overlap(self, axis):
        if axis[0][1] != axis[1][1]:
            return axis[2][0] - axis[1][0]
        else:
            return 0