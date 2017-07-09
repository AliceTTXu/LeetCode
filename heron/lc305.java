public class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {

        // List for storing the result
        List<Integer> res = new ArrayList<Integer>();

        // Integer for counting the lands we found so far
        int lands = 0;

        // Integer mapping for getting the root index of each position
        int[] rootMap = new int[m * n];

        // Initializes the rootMap with -1
        Arrays.fill(rootMap, -1);

        for (int i = 0; i < positions.length; i++) {

            int row = positions[i][0];
            int col = positions[i][1];

            // Gets root set from neighbors
            Set<Integer> rootSet = getRootSetOfNeighbors(rootMap, row, col, n, m);

            // Updates the rootMap
            int index = row * n + col;
            for (Integer root : rootSet) {
                rootMap[root] = index;
            }
            rootMap[index] = index;

            // Calculates
            lands = lands - rootSet.size() + 1;
            res.add(lands);

        }
        return res;

    }

    private Set<Integer> getRootSetOfNeighbors(int[] rootMap, int row, int col, int n, int m) {
        Set<Integer> rootSet = new HashSet<>();
        if (row > 0 && rootMap[(row-1) * n + col] != -1) {  // Left
            rootSet.add(getRoot(rootMap, (row-1) * n + col));
        }
        if (row < m-1 && rootMap[(row+1) * n + col] != -1) {    // Right
            rootSet.add(getRoot(rootMap, (row+1) * n + col));
        }
        if (col > 0 && rootMap[row * n + (col-1)] != -1) {  // Up
            rootSet.add(getRoot(rootMap, row * n + (col-1)));
        }
        if (col < n-1 && rootMap[row * n + (col+1)] != -1) {    // Down
            rootSet.add(getRoot(rootMap, row * n + (col+1)));
        }
        return rootSet;
    }

    private int getRoot(int[] rootMap, int index) {
        while(rootMap[index] != index) {
            index = rootMap[index];
        }
        return index;
    }

}
