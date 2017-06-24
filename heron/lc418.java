public class Solution {
    public int wordsTyping(String[] sentence, int rows, int cols) {

        // O(m+n)

        // s = "a _ b c d _ e "
        // adj= 0 1 0 -1-21 0

        String s = String.join(" ", sentence) + " ";
        int len = s.length();
        int[] adj = new int[len];

        // Builds adjustment array
        for (int i=1; i<len; i++) {
            adj[i] = (s.charAt(i) == ' ') ? 1 : adj[i-1] - 1;
        }

        // Counts
        int pos = 0;
        for (int i=0; i<rows; i++) {
            pos += cols;
            pos += adj[pos % len];
        }

        // Picks the lower bound as the incomplete ones can't be counted
        return pos / len;

    }
}
