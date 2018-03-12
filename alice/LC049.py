class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        mapping = {}

        for x in strs:
            chars = list(x)
            chars.sort()
            key = "".join(chars)
            if key not in mapping:
                mapping[key] = [x]
            else:
                mapping[key].append(x)
        return mapping.values()

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print s.groupAnagrams([])
print s.groupAnagrams(["aaaad", "aadaa", "sdfdg"])
print s.groupAnagrams(["ada", "daa", "aad"])