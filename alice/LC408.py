class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        
        if word and not abbr or not word and abbr:
            return False
        
        n = 0
        index = 0
        for x in abbr:
            if x >= '0' and x <= '9':
                if n == 0 and x == '0':
                    return False
                n = n * 10 + int(x)
            else:                
                index += n
                n = 0
                if index > len(word) - 1 or x != word[index]:
                    return False
                index += 1

        return n == (len(word) - index)