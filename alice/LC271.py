class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """

        return ''.join([str(len(x)) + '|' + x for x in strs])

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """

        out = []
        while s:
            index = s.index('|')
            out.append(s[index + 1:index + 1 + int(s[:index])])
            s = s[index + 1 + int(s[:index]):]

        return out

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# print codec.encode([""])
# print codec.decode(codec.encode([""]))