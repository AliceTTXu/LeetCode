class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        in_S = S.split()
        result = []
        counts = 1
        for x in in_S:
            if x[0].lower() in set(['a', 'e', 'i', 'o', 'u']):
                result.append(x + 'ma' + 'a' * counts + ' ')
            else:
                result.append(x[1:] + x[0] + 'ma' + 'a' * counts + ' ')
            counts += 1
            
        return ''.join(result)[:-1] if result else ''
