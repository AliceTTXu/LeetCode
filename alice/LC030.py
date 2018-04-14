class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        len_word = len(words[0])
        len_concatenation = len(words) * len_word
        out = []

        words_dict = {}
        for x in words:
            words_dict[x] = words_dict.get(x, 0) + 1

        for i in range(len(s) - len_concatenation + 1):
            start_index = current_index = i
            temp_dict = {}
            hit = 0
            while current_index + len_word <= len(s):
                one_word = s[current_index:current_index + len_word]
                current_index += len_word
                if one_word in words_dict:
                    temp_dict[one_word] = temp_dict.get(one_word, 0) + 1
                    hit += 1

                    while temp_dict[one_word] > words_dict[one_word]:
                        temp_dict[s[start_index:start_index + len_word]] -= 1
                        start_index += len_word
                        hit -= 1

                    if hit == len(words):
                        out.append(start_index)
                    
                else:
                    break

        return out


    def findSubstring_BF(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        all_concatenation = set(self.permutation(words))
        len_concatenation = len(words) * len(words[0])
        start_index = 0
        out = []

        while len(s) - start_index >= len_concatenation:
            if s[start_index:start_index + len_concatenation] in all_concatenation:
                out.append(start_index)
            start_index += 1

        return out

    def permutation(self, li):
        if len(li) == 1:
            return li

        out = []

        for i, x in enumerate(li):
            out += [x + y for y in self.permutation(li[:i] + li[i + 1:])]

        return out

s = Solution()
print s.findSubstring("aaaaaaaa", ["aa","aa","aa"])

