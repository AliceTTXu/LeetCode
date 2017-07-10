public class Solution {

    int[] dRow = {1, -1, 0, 0};
    int[] dCol = {0, 0, 1, -1};

    public int longestIncreasingPath(int[][] matrix) {

        // Checks if the input is valid
        if (matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dis = new int[m][n];

        // Runs DFS on each position
        int max = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                max = Math.max(max, dfs(matrix, dis, i, j, m, n));
            }
        }

        return max;

    }

    int dfs(int[][] matrix, int[][] dis, int row, int col, int m, int n) {

        // If visit already, return the distance found before
        if (dis[row][col] != 0) {
            return dis[row][col];
        }

        // Search each neighbers (left, right, top, bottom)
        for (int i = 0; i < 4; i++) {
            int nRow = row + dRow[i];
            int nCol = col + dCol[i];
            if (nRow >= 0 && nRow < m && nCol >= 0 && nCol < n && matrix[nRow][nCol] > matrix[row][col]) {
                dis[row][col] = Math.max(dis[row][col], dfs(matrix, dis, nRow, nCol, m, n));
            }
        }

        // Add one on distnace
        return ++dis[row][col];

    }

}
