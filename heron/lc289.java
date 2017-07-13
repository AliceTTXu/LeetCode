public class Solution {

    private int[] dRow = new int[]{-1, -1, -1, 0, 0, 1, 1, 1};
    private int[] dCol = new int[]{-1, 0, 1, -1, 1, -1, 0, 1};

    public void gameOfLife(int[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) {
            return;
        }
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int neighbors = getNeighbors(board, i, j, m, n);
                if (board[i][j] == 1 && (neighbors == 2 || neighbors == 3)) {
                    board[i][j] += 10;
                }
                if (board[i][j] == 0 && neighbors == 3) {
                    board[i][j] += 10;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] /= 10;
            }
        }
    }

    private int getNeighbors(int[][] board, int row, int col, int m, int n) {
        int neighbors = 0;
        for (int i = 0; i < 8; i++) {
            int nRow = row + dRow[i];
            int nCol = col + dCol[i];
            if (nRow >= 0 && nRow < m && nCol >= 0 && nCol <n) {
                neighbors += ((board[nRow][nCol] % 10 == 1) ? 1 : 0);
            }
        }
        return neighbors;
    }
}
