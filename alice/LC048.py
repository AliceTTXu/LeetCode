class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in xrange(n):
            matrix.append([x[i] for x in matrix[:n]][::-1])
        for i in xrange(n):
            matrix.pop(0)

    def rotate2(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        

s = Solution()
print s.rotate([[1,2,3], [4,5,6], [7,8,9]])
print s.rotate([[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]])
