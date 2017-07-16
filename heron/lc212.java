public class Solution {

    private Set<String> resultSet = new HashSet<>();

    public List<String> findWords(char[][] board, String[] words) {

        // Builds the trie
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }

        // Searches
        int m = board.length;
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                searchAt(board, "", i, j, trie, m, n, visited);
            }
        }

        return new ArrayList<String>(resultSet);
    }

    private void searchAt(char[][] board, String word, int row, int col, Trie trie, int m, int n, boolean[][] visited) {

        // If out of bound or visted, stops here
        if (!((row >= 0 && row < m) && (col >= 0 && col < n)) || visited[row][col]) {
            return;
        }

        // Gets the new word
        word = word + board[row][col];

        // No word in dictionary starts with this string, stops here
        if (!trie.containsStartWith(word)) {
            return;
        }

        // If the dictionary contains the word we have so far, saves to the result set
        if (trie.contains(word)) {
            resultSet.add(word);
        }

        // Goes to next position from here
        visited[row][col] = true;
        searchAt(board, word, row + 1, col, trie, m, n, visited);
        searchAt(board, word, row - 1, col, trie, m, n, visited);
        searchAt(board, word, row, col + 1, trie, m, n, visited);
        searchAt(board, word, row, col - 1, trie, m, n, visited);
        visited[row][col] = false;

    }


    class TrieNode {
        public TrieNode[] children = new TrieNode[26];
        public String item = "";
    }

    class Trie {

        private TrieNode root = new TrieNode();

        public void insert(String word) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                if (node.children[c - 'a'] == null) {
                    node.children[c - 'a'] = new TrieNode();
                }
                node = node.children[c - 'a'];
            }
            node.item = word;
        }

        public boolean containsStartWith(String prefix) {
            TrieNode node = root;
            for (char c : prefix.toCharArray()) {
                if (node.children[c - 'a'] == null) {
                    return false;
                }
                node = node.children[c - 'a'];
            }
            return true;
        }

        public boolean contains(String word) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                if (node.children[c - 'a'] == null) {
                    return false;
                }
                node = node.children[c - 'a'];
            }
            return node.item.equals(word);
        }

    }

}
