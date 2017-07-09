public class Solution {
    public void wallsAndGates(int[][] rooms) {

        if (rooms == null || rooms.length == 0 || rooms[0].length == 0) {
            return;
        }

        Queue<int[]> queue = new LinkedList<>();
        int n = rooms.length;
        int m = rooms[0].length;

        // Pushs all the gates into the queue
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (rooms[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        // Starts BFS
        while(!queue.isEmpty()) {
            int[] toVisit = queue.poll();
            int pi = toVisit[0];
            int pj = toVisit[1];
            if (pi > 0 && rooms[pi-1][pj] == Integer.MAX_VALUE) {
                rooms[pi-1][pj] = rooms[pi][pj] + 1;
                queue.offer(new int[]{pi-1, pj});
            }
            if (pi < n-1 && rooms[pi+1][pj] == Integer.MAX_VALUE) {
                rooms[pi+1][pj] = rooms[pi][pj] + 1;
                queue.offer(new int[]{pi+1, pj});
            }
            if (pj > 0 && rooms[pi][pj-1] == Integer.MAX_VALUE) {
                rooms[pi][pj-1] = rooms[pi][pj] + 1;
                queue.offer(new int[]{pi, pj-1});
            }
            if (pj < m-1 && rooms[pi][pj+1] == Integer.MAX_VALUE) {
                rooms[pi][pj+1] = rooms[pi][pj] + 1;
                queue.offer(new int[]{pi, pj+1});
            }
        }

    }
}
