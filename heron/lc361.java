public class Solution {
    public int maxKilledEnemies(char[][] grid) {

        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int m = grid.length;
        int n = grid[0].length;

        int max = 0;
        int row = 0;
        int[] col = new int[n];

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 'W') {
                    continue;
                }
                if (i == 0 || grid[i-1][j] == 'W') {
                    col[j] = findKillsOnCol(grid, i, j, m, n);
                }
                if (j == 0 || grid[i][j-1] == 'W') {
                    row = findKillsOnRow(grid, i, j, m, n);
                }
                if (grid[i][j] == '0') {
                    // Bomb can only be put on empty spot
                    max = Math.max(max, col[j] + row);
                }
            }
        }

        return max;

    }

    private int findKillsOnCol(char[][] grid, int pi, int pj, int m, int n) {
        int res = 0;
        for (int i=pi; i<m && grid[i][pj] != 'W'; i++) {
            if (grid[i][pj] == 'E') {
                res ++;
            }
        }
        return res;
    }

    private int findKillsOnRow(char[][] grid, int pi, int pj, int m, int n) {
        int res = 0;
        for (int j=pj; j<n && grid[pi][j] != 'W'; j++) {
            if (grid[pi][j] == 'E') {
                res ++;
            }
        }
        return res;
    }
}
