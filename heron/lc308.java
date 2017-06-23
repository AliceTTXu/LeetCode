public class NumMatrix {

    int[][] mMatrix;

    int m;
    int n;

    public NumMatrix(int[][] matrix) {

        // Returns if the input matrix is empty
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }

        // Stores the class properties
        mMatrix = matrix;
        m = matrix.length;
        n = matrix[0].length;

        // Calculates matrix[i][j] = matrix[i][0] + matrix[i][1] ... + matrix[i][j]
        for (int i=0; i<m; i++) {
            for (int j=1; j<n; j++) {
                mMatrix[i][j] += mMatrix[i][j-1];
            }
        }

    }

    // O(n)
    public void update(int row, int col, int val) {

        int originalValue = (col == 0) ? mMatrix[row][0] : mMatrix[row][col] - mMatrix[row][col-1];
        int delta = val - originalValue;

        for (int j=col; j<n; j++) {
            mMatrix[row][j] += delta;
        }

    }

    // O(m)
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int result = 0;
        for (int i=row1; i<=row2; i++) {
            result += (col1 == 0) ? mMatrix[i][col2] : mMatrix[i][col2] - mMatrix[i][col1-1];
        }
        return result;
    }

}
