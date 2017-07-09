public class Solution {
    public boolean isRectangleCover(int[][] rectangles) {

        // If empty, returns false
        if (rectangles.length == 0 || rectangles[0].length == 0) {
            return false;
        }

        int x1 = Integer.MAX_VALUE;
        int y1 = Integer.MAX_VALUE;
        int x2 = Integer.MIN_VALUE;
        int y2 = Integer.MIN_VALUE;

        int areaSum = 0;
        Set<String> dots = new HashSet<>();
        for (int[] r : rectangles) {

            // Updates the bounding box corners
            x1 = Math.min(x1, r[0]);
            y1 = Math.min(y1, r[1]);
            x2 = Math.max(x2, r[2]);
            y2 = Math.max(y2, r[3]);

            // Updates the sum of areas
            areaSum += (r[2] - r[0]) * (r[3] - r[1]);

            // Updates the dot set
            String s1 = r[0] + "-" + r[1];
            String s2 = r[0] + "-" + r[3];
            String s3 = r[2] + "-" + r[1];
            String s4 = r[2] + "-" + r[3];

            if (!dots.add(s1)) {
                dots.remove(s1);
            }
            if (!dots.add(s2)) {
                dots.remove(s2);
            }
            if (!dots.add(s3)) {
                dots.remove(s3);
            }
            if (!dots.add(s4)) {
                dots.remove(s4);
            }

        }

        // Checks the final four corner dots
        String s1 = x1 + "-" + y1;
        String s2 = x1 + "-" + y2;
        String s3 = x2 + "-" + y1;
        String s4 = x2 + "-" + y2;
        if (!dots.contains(s1)
           || !dots.contains(s2)
           || !dots.contains(s3)
           || !dots.contains(s4)
           || dots.size() != 4) {
            return false;
        }

        // Checks if the area sum is correct
        return areaSum == (x2 - x1) * (y2 - y1);

    }
}
