public class Solution {
    public int threeSumSmaller(int[] nums, int target) {

        int len = nums.length;
        int count = 0;
        Arrays.sort(nums);

        for (int i=0; i<len-2; i++) {
            int l = i+1;
            int r = len-1;
            while(l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum < target) {
                    // All the combination of l to r, r-1, ... l+1 counts
                    count += r - l;
                    l++;
                } else {
                    r--;
                }
            }
        }

        return count;

    }
}
