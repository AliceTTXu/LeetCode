public class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int m = grid.length;
        int n = grid[0].length;

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    searchAndRemove(grid, i, j, m, n);
                    count ++;
                }
            }
        }

        return count;
    }

    private void searchAndRemove(char[][] grid, int row, int col, int m, int n) {
        if (!(row >= 0 && row < m) || !(col >= 0 && col < n)) {
            return;
        }
        if (grid[row][col] == '0') {
            return;
        }
        grid[row][col] = '0';
        searchAndRemove(grid, row + 1, col, m, n);
        searchAndRemove(grid, row - 1, col, m, n);
        searchAndRemove(grid, row, col + 1, m, n);
        searchAndRemove(grid, row, col - 1, m, n);
    }

}
