public class Solution {
    public int hIndex(int[] citations) {

        int len = citations.length;
        int[] counts = new int[len + 1];

        // put into buckets
        for (int c : citations) {
            if (c > len) {
                counts[len] ++;
            } else {
                counts[c] ++;
            }
        }

        // get the largest
        int total = 0;
        for (int i=len; i>=0 ; i--) {
            total += counts[i];
            if (total >= i) {
                return i;
            }
        }

        return 0;

    }
}
