public class Solution {

    private int[] dR = new int[]{1, -1, 0, 0};
    private int[] dC = new int[]{0, 0, 1, -1};

    public boolean exist(char[][] board, String word) {
        if (board == null || board.length == 0 || board[0].length == 0) {
            return false;
        }
        int m = board.length;
        int n = board[0].length;
        boolean visited[][] = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (searchAt(word, board, i, j, m, n, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean searchAt(String word, char[][] board, int row, int col, int m, int n, boolean[][] visited) {
        if (word.length() == 0) {
            return true;
        }
        if (!((row >= 0 && row < m) && (col >= 0 && col < n)) || visited[row][col]) {
            return false;
        }
        if (word.charAt(0) != board[row][col]) {
            return false;
        }
        visited[row][col] = true;
        for (int i = 0; i< 4; i++) {
            int nR = row + dR[i];
            int nC = col + dC[i];
            String subWord = word.substring(1);
            if (searchAt(subWord, board, nR, nC, m, n, visited)) {
                return true;
            }
        }
        visited[row][col] = false;
        return false;
    }

}
