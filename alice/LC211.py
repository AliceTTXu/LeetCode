class TrieNode:

    def __init__(self, character):
        self.character = character
        self.children = {}
        self.is_leaf = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode(None)

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        return self.__search_helper(word, self.root)
    
    def __search_helper(self, word, root):
        current_node = root
        for i, w in enumerate(word):
            if w == '.':                
                return any([self.__search_helper(word[i + 1:], current_node.children[c]) for c in current_node.children])
            elif w in current_node.children:
                current_node = current_node.children[w]
            else:
                return False

        return current_node.is_leaf

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)