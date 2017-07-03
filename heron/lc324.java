public class Solution {
    public void wiggleSort(int[] nums) {

        int len = nums.length;
        int l = (len + 1)/2;
        int r = len;

        int[] copy = new int[len];
		Arrays.sort(nums);
        System.arraycopy(nums, 0, copy, 0, len);


        for (int i=0; i<len; i++) {
            nums[i] = i % 2 == 0 ? copy[--l] : copy[--r];
        }

    }
}
