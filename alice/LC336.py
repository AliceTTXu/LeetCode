class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        mapping = {word: i for i, word in enumerate(words)}
        out = []

        def is_palindrome(word):
            return word == word[::-1]

        for word in words:
            for i in xrange(len(word) + 1):
                left = word[:i]
                right = word[i:]
                if is_palindrome(left) and right[::-1] in mapping:
                    if mapping[right[::-1]] != mapping[word]:
                        out.append([mapping[right[::-1]], mapping[word]])
                if i != len(word) and is_palindrome(right) and left[::-1] in mapping:
                    if mapping[word] != mapping[left[::-1]]:
                        out.append([mapping[word], mapping[left[::-1]]])

        return out