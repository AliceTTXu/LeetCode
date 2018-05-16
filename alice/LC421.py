class TrieNode:
    
    def __init__(self):
        self.zero = None
        self.one = None

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        root = TrieNode()
        
        for num in nums:
            num_b = bin(num)[2:].zfill(31)
            current_node = root
            for n in num_b:
                if n == '0':
                    if not current_node.zero:
                        current_node.zero = TrieNode()
                    current_node = current_node.zero
                else:
                    if not current_node.one:
                        current_node.one = TrieNode()
                    current_node = current_node.one

        out = 0

        for num in nums:
            num_b = bin(num)[2:].zfill(31)
            current_node = root
            temp_out = 0
            for i, n in enumerate(num_b):
                if n == '0':
                    if not current_node.one:
                        current_node = current_node.zero
                    else:
                        current_node = current_node.one
                        temp_out += 2 ** (30 - i)
                else:
                    if not current_node.zero:
                        current_node = current_node.one
                    else:
                        current_node = current_node.zero
                        temp_out +=  2 ** (30 - i)
                out = max(out, temp_out)

        return out
