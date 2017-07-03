public class Solution {

    private Set<List<Integer>> resultSet;

    public List<List<Integer>> threeSum(int[] nums) {

        resultSet = new HashSet<>();

        // First, sorts the input array
        Arrays.sort(nums);

        // Then, moves the iterator
        for (int i=0; i<nums.length-2; i++) {
            int l = i + 1;
            int r = nums.length - 1;

            while(l < r) {
                // Finally, we get the combinations
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    // Saves the result here
                    saveResult(nums, i, l, r);
                    l++;
                    r--;
                } else if (sum > 0) {
                    r--;
                } else {
                    l++;
                }
            }

        }

        // Converts the set to array
        List<List<Integer>> results = new ArrayList<>();
        results.addAll(resultSet);
        return results;

    }

    private void saveResult(int[] nums, int p1, int p2, int p3) {
        List<Integer> result = new ArrayList<>();
        result.add(nums[p1]);
        result.add(nums[p2]);
        result.add(nums[p3]);
        resultSet.add(result);
    }

}
