public class Solution {

    int[][] numReach;
    int[][] distance;

    public int shortestDistance(int[][] grid) {

        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return -1;
        }

        int numBuilding = 0;

        int m = grid.length;
        int n = grid[0].length;

        numReach = new int[m][n];
        distance = new int[m][n];

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 1) { // if building
                    boolean[][] visited = new boolean[m][n];
                    LinkedList<Integer> queue = new LinkedList<>();
                    dfs(grid, i, j, i, j, visited, queue, 0);
                    numBuilding ++;
                }
            }
        }

        int result = Integer.MAX_VALUE;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 0 && numReach[i][j] == numBuilding) {
                    result = Math.min(result, distance[i][j]);
                }
            }
        }
        return result == Integer.MAX_VALUE ? -1 : result;

    }

    private void dfs(int[][] grid, int oi, int oj, int i, int j, boolean[][] visited, LinkedList<Integer> queue, int distanceSoFar) {

        visit(grid, oi, oj, i, j, visited, queue, distanceSoFar);

        int n = grid[0].length;

        while(!queue.isEmpty()) {
            int size = queue.size();
            distanceSoFar++;
            for (int k=0; k<size; k++) {
                int top = queue.poll();
                i = top / n;
                j = top % n;
                visit(grid, oi, oj, i+1, j, visited, queue, distanceSoFar);
                visit(grid, oi, oj, i-1, j, visited, queue, distanceSoFar);
                visit(grid, oi, oj, i, j+1, visited, queue, distanceSoFar);
                visit(grid, oi, oj, i, j-1, visited, queue, distanceSoFar);
            }
        }

    }

    private void visit(int[][] grid, int oi, int oj, int i, int j, boolean[][] visited, LinkedList<Integer> queue, int distanceSoFar) {

        int m = grid.length;
        int n = grid[0].length;

        if(i<0 || i>=m || j<0 || j>=n || visited[i][j]) {
            return;
        }

        if((!(i==oi && j==oj)) && grid[i][j] != 0) {
            return;
        }

        numReach[i][j] ++;
        visited[i][j] = true;
        distance[i][j] += distanceSoFar;
        queue.offer(i*n+j);

    }
}
