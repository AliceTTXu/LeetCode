class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except IndexError:
                    return False

        return True