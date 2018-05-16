class TrieNode:
    
    def __init__(self, character):
        self.is_leaf = False
        self.children = {}
        self.character = character

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        root = TrieNode(None)
        
        for word in dict:
            current_node = root
            for w in word:
                if w in current_node.children:
                    current_node = current_node.children[w]
                else:
                    temp_node = TrieNode(w)
                    current_node.children[w] = temp_node
                    current_node = temp_node
            current_node.is_leaf = True

        sentence_list = sentence.split(' ')

        for i, word in enumerate(sentence_list):
            current_node = root
            temp_prefix = ''
            for w in word:
                if w not in current_node.children:
                    break
                current_node = current_node.children[w]
                temp_prefix += w
                if current_node.is_leaf:
                    sentence_list[i] = temp_prefix
                    break

        return ' '.join(sentence_list)
