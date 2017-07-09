public class Solution {

    private class Point implements Comparable<Point> {

        int x;
        int h;
        boolean isLeft;

        Point(int x, int h, boolean isLeft) {
            this.x = x;
            this.h = h;
            this.isLeft = isLeft;
        }

        private int getSignedH() {
            return (isLeft) ? h : -h;
        }

        @Override
        public int compareTo(Point p) {
            if (this.x != p.x) {
                return this.x - p.x;
            } else {
                return p.getSignedH() - this.getSignedH();
            }
        }

    }

    public List<int[]> getSkyline(int[][] buildings) {

        // Initials the lists
        List<int[]> result = new ArrayList<>();
        List<Point> points = new ArrayList<>();

        // Builds the point list
        for (int[] b : buildings) {
            points.add(new Point(b[0], b[2], true));
            points.add(new Point(b[1], b[2], false));
        }

        // Sorts the points
        Collections.sort(points);

        // Builds the queue
        Queue<Integer> heightQueue = new PriorityQueue<>(new Comparator<Integer>() {
            public int compare(Integer h1, Integer h2) {
                return h2 - h1;
            }
        });

        // Puts the ground floor
        heightQueue.offer(0);

        // Walks through the points
        int prev = 0;
        for (Point p : points) {

            // Updates the queue
            if (p.isLeft) {
                heightQueue.offer(p.h);
            } else {
                heightQueue.remove(p.h);
            }

            // Updates the result
            int cur = heightQueue.peek();
            if (cur != prev) {
                result.add(new int[]{p.x, cur});
                prev = cur;
            }

        }

        // Ends here
        return result;

    }
}
