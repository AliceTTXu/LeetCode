class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        index_dict = {}
        for i, x in enumerate(B):
            index_dict[x] = index_dict.get(x, []) + [i]

        out = []
        for x in A:
            out.append(index_dict[x].pop())

        return out