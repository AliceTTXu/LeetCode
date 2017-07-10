public class Solution {

    private int[] dx = {0, 0, 1, -1};
    private int[] dy = {1, -1, 0, 0};

    public List<int[]> pacificAtlantic(int[][] matrix) {

        List<int[]> result = new ArrayList<>();

        // Checks for invalid input
        if (matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        boolean[][] P = new boolean[m][n];
        boolean[][] A = new boolean[m][n];

        // Flows from X asix
        for (int i = 0; i < m; i++) {
            flow(matrix, P, i, 0, m, n);
            flow(matrix, A, i, n-1, m, n);
        }

        // Flows from Y asix
        for (int j = 0; j < n; j++) {
            flow(matrix, P, 0, j, m, n);
            flow(matrix, A, m-1, j, m, n);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (P[i][j] && A[i][j]) {
                    result.add(new int[]{i, j});
                }
            }
        }

        return result;

    }

    private void flow(int[][] matrix, boolean[][] visited, int row, int col, int m, int n) {

        if (visited[row][col]) {
            return;
        }

        visited[row][col] = true;
        for (int i = 0; i < 4; i++) {
            int nRow = row + dy[i];
            int nCol = col + dx[i];
            if (nRow >= 0 && nRow < m && nCol >= 0 && nCol < n && matrix[nRow][nCol] >= matrix[row][col]) {
                flow(matrix, visited, nRow, nCol, m, n);
            }
        }

    }


}
