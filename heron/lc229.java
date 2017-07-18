public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> result = new ArrayList<>();

        Integer n1 = null;
        Integer n2 = null;
        int c1 = 0;
        int c2 = 0;

        for (int n : nums) {
            if (n1 != null && n == n1.intValue()) {
                c1 ++;
            } else if (n2 != null && n == n2.intValue()) {
                c2 ++;
            } else if (c1 == 0) {
                c1 = 1;
                n1 = n;
            } else if (c2 == 0) {
                c2 = 1;
                n2 = n;
            } else {
                c1 --;
                c2 --;
            }
        }

        c1 = 0;
        c2 = 0;

        for (int n : nums) {
            if (n == n1.intValue()) {
                c1 ++;
            } else if (n == n2.intValue()) {
                c2 ++;
            }
        }

        if (c1 > nums.length / 3) {
            result.add(n1);
        }

        if (c2 > nums.length / 3) {
            result.add(n2);
        }

        return result;

    }
}
