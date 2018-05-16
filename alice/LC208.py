class TrieNode:

    def __init__(self, character):
        self.is_leaf = False
        self.children = {}
        self.character = character

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        current_node = self.root
        for w in word:
            if w in current_node.children:
                current_node = current_node.children[w]
            else:
                temp_node = TrieNode(w)
                current_node.children[w] = temp_node
                current_node = temp_node

        current_node.is_leaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        current_node = self.root
        for w in word:
            if w in current_node.children:
                current_node = current_node.children[w]
            else:
                return False

        return current_node.is_leaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        current_node = self.root
        for w in prefix:
            if w in current_node.children:
                current_node = current_node.children[w]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)