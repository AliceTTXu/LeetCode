public class Solution {
    public int numberOfPatterns(int m, int n) {

        // Builds the skip table
        int[][] skip = new int[10][10];
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5;

        // Builds the visit list
        boolean[] visit = new boolean[10];

        // DFS for the result
        int res = 0;
        for (int i=m; i<=n; i++) {
            res += dfs(visit, skip, i-1, 1) * 4;    // Corner
            res += dfs(visit, skip, i-1, 2) * 4;    // Edge
            res += dfs(visit, skip, i-1, 5);        // Center
        }

        // done
        return res;

    }

    private int dfs(boolean[] visit, int[][] skip, int remain, int cur) {

        // Terminates
        if (remain < 0) {
            return 0;
        }
        if (remain == 0) {
            return 1;
        }

        // Marks as visited (NOTE: easy to forget)
        visit[cur] = true;

        // Searches at next level
        int res = 0;
        for (int i=1; i<=9; i++) {
            if (!visit[i] && (skip[cur][i] == 0 || visit[skip[cur][i]])) {
                res += dfs(visit, skip, remain-1, i);
            }
        }

        // Unmakrs visited (NOTE: easy to forget)
        visit[cur] = false;

        // Returns what is found
        return res;

    }


}
