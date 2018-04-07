import collections

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        out = 0
        distinct = 0
        counts = collections.Counter()

        left = right = 0

        while right < len(s):
            counts[s[right]] += 1
            if counts[s[right]] == 1:
                distinct += 1
                while distinct > k:
                    counts[s[left]] -= 1
                    if counts[s[left]] == 0:
                        distinct -= 1
                    left += 1
            out = max(out, (right - left + 1))
            right += 1

        return out
