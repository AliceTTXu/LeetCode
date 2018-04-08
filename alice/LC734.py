import collections
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        if len(words1) != len(words2):
            return False
        
        pairs_dict = collections.defaultdict(set)
        for x in pairs:
            pairs_dict[x[0]].add(x[1])
            pairs_dict[x[1]].add(x[0])

        for x, y in zip(words1, words2):
            if x == y or y in pairs_dict[x]:
                continue
            else:
                return False

        return True