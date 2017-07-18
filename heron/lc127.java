public class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        Set<String> words = new HashSet<>(wordList);
        Queue<String> queue = new LinkedList<>();

        queue.add(beginWord);
        int len = 0;

        while(!queue.isEmpty()) {
            int size = queue.size();
            len ++;
            for (int i = 0; i < size; i++) {
                String curWord = queue.poll();
                if (curWord.equals(endWord)) {
                    return len;
                }
                for (String nextWord : getNextWord(curWord, words)) {
                    queue.offer(nextWord);
                }
            }
        }

        return 0;

    }

    private Set<String> getNextWord(String s, Set<String> words) {
        char[] chars = s.toCharArray();
        Set<String> result = new HashSet<>();
        for (int i = 0; i < chars.length; i++) {
            char c = s.charAt(i);
            for (char x = 'a'; x < 'z'; x++) {
                if (x == c) {
                    continue;
                }
                chars[i] = x;
                String nextWord = new String(chars);
                if (words.contains(nextWord)) {
                    result.add(nextWord);
                    words.remove(nextWord);
                }
                chars[i] = c;
            }
        }
        return result;
    }
}
