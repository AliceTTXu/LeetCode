public class Solution {
    public void wiggleSort(int[] nums) {
        for (int i=0; i<nums.length; i++) {
            if (i%2 == 1) {
                if (nums[i-1] > nums[i]) {
                    swap(nums, i);
                }
            } else {
                if (i!=0 && (nums[i-1] < nums[i])) {
                    swap(nums, i);
                }
            }
        }
    }

    private void swap(int[] nums, int i) {
        int t = nums[i];
        nums[i] = nums[i-1];
        nums[i-1] = t;
    }
}
