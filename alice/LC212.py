class TrieNode:
    
    def __init__(self, character):
        self.character = character
        self.children = {}
        self.is_leaf = False

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        if not words or not board or not board[0]:
            return []

        root = TrieNode(None)

        for word in words:
            current_node = root
            for w in word:
                if w not in current_node.children:
                    temp_node = TrieNode(w)
                    current_node.children[w] = temp_node
                current_node = current_node.children[w]
            current_node.is_leaf = True

        self.out = set()
        self.N = len(board)
        self.M = len(board[0])
        self.board = board

        for i in xrange(self.N):
            for j in xrange(self.M):
                if self.board[i][j] in root.children:
                    # print i, j, self.board[i][j], root.children[self.board[i][j]].character
                    self.__dfs(i, j, self.board[i][j], root.children[self.board[i][j]], set())

        return list(self.out)

    def __dfs(self, i, j, prefix, node, seen):
        # print i, j, prefix, node, seen
        if node.is_leaf:
            # print prefix, self.board[i][j], node.character
            self.out.add(prefix)
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for move in moves:
            x = i + move[0]
            y = j + move[1]
            if 0 <= x < self.N and 0 <= y < self.M and (x, y) not in seen:
                next_char = self.board[x][y]
                
                # print i, j, x, y, next_char, node.children.keys()
                if next_char in node.children:
                    # if len(prefix) > 16: print x, y, prefix + next_char, node.children.keys()
                    seen.add((i, j))
                    self.__dfs(x, y, prefix + next_char, node.children[next_char], seen)
                    seen.remove((i, j))
