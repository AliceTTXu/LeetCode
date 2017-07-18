public class Solution {
    public int majorityElement(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int majority = nums[0];
        int count = 0;
        for (int n : nums) {
            if (majority != n) {
                count --;
            } else {
                count ++;
            }
            if (count < 0) {
                majority = n;
                count = 0;
            }
        }
        return majority;
    }
}
