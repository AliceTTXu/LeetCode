import collections

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        
        if len(words1) != len(words2):
            return False
        
        pairs_dict = collections.defaultdict(list)
        for x in pairs:
            pairs_dict[x[0]].append(x[1])
            pairs_dict[x[1]].append(x[0])

        def is_similar(w1, w2):
            stack = [w1]
            seen = set()
            while stack:
                temp = stack.pop()
                if temp == w2:
                    return True
                else:
                    seen.add(temp)
                    for x in pairs_dict[temp]:
                        if x not in seen:
                            stack.append(x)
            return False

        for x, y in zip(words1, words2):
            if not is_similar(x, y):
                return False

        return True