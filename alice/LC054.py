class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        out = []

        while matrix:
            out.extend(matrix.pop(0))
            if matrix:
                out.extend([x.pop() for x in matrix])
            else:
                break
            if matrix[0] == []:
                break
            out.extend(matrix.pop()[::-1])
            if matrix:
                out.extend([x.pop(0) for x in matrix][::-1])
            else:
                break

        return out