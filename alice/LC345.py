class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        l, r = 0, len(s) - 1
        vowel = set(['a', 'e', 'i', 'o', 'u'])

        while l < r:
            while s[l].lower() not in vowel:
                l += 1
                if l >= len(s):
                    break
            while s[r].lower() not in vowel:
                r -= 1
                if r <= 0:
                    break
            if l < r:
                s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)