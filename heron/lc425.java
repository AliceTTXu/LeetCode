public class Solution {
    public List<List<String>> wordSquares(String[] words) {

        List<List<String>> ans = new ArrayList<>();
        if (words == null || words.length == 0) {
            return ans;
        }

        List<String> ansBuilder = new ArrayList<String>();
        // you can't use len = words.length (more words may be provided)
        int len = words[0].length();
        Trie trie = new Trie(words);
        for (String w : words) {
            ansBuilder.add(w);
            search(len, trie, ans, ansBuilder);
            ansBuilder.remove(ansBuilder.size()-1);
        }

        return ans;

    }

    public void search(int len, Trie trie, List<List<String>> ans, List<String> ansBuilder) {
        if (ansBuilder.size() == len) {
            ans.add(new ArrayList<>(ansBuilder));
            return;
        }
        StringBuilder prefixBuilder = new StringBuilder();
        int idx = ansBuilder.size();
        for (String w : ansBuilder) {
            prefixBuilder.append(w.charAt(idx));
        }
        for (String sw : trie.findWordsByPrefix(prefixBuilder.toString())) {
            ansBuilder.add(sw);
            search(len, trie, ans, ansBuilder);
            ansBuilder.remove(ansBuilder.size()-1);
        }
    }

    class Trie {

        TrieNode root;

        Trie(String[] words) {
            root = new TrieNode();
            for (String w : words) {
                TrieNode cur = root;
                for (char c : w.toCharArray()) {
                    int i = c - 'a';
                    if (cur.children[i] == null) {
                        cur.children[i] = new TrieNode();
                    }
                    cur.children[i].startWith.add(w);
                    cur = cur.children[i];
                }
            }
        }

        List<String> findWordsByPrefix(String prefix) {
            List<String> ans = new ArrayList<String>();
            TrieNode cur = root;
            for (char c : prefix.toCharArray()) {
                int i = c - 'a';
                if (cur.children[i] == null) {
                    return ans;
                }
                cur = cur.children[i];
            }
            ans.addAll(cur.startWith);
            return ans;
        }

    }

    class TrieNode {
        List<String> startWith;
        TrieNode[] children;
        TrieNode() {
            startWith = new ArrayList<String>();
            children = new TrieNode[26];
        }
    }

}
