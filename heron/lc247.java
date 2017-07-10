public class Solution {
    public List<String> findStrobogrammatic(int n) {
        // Runs the recursive helper function
        return f(n, n);
    }

    private List<String> f(int n, int m) {

        // Initialize the result container
        List<String> res = new ArrayList<>();

        // If the n is 0, return empty string
        if (n == 0) {
            res.add("");
            return res;
        }

        // If the n is 1, return 0, 1, 8
        if (n == 1) {
            res.add("0");
            res.add("1");
            res.add("8");
            return res;
        }

        // Otherwise, grab result of n-2, append, then save to result
        List<String> resLow = f(n - 2, m);
        for (String s : resLow) {
            // If we are not currently doing the left most digit
            if (n != m) {
                res.add("0" + s + "0");
            }
            res.add("1" + s + "1");
            res.add("8" + s + "8");
            res.add("6" + s + "9");
            res.add("9" + s + "6");
        }

        // Ends here
        return res;

    }
}
