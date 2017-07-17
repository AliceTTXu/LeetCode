public class Solution {
    public String encode(String s) {

        // NOTE: always uses the string in dp for calculation or replacement, which is the shortest we have so far

        // Checks for invalid inputs
        if (s == null || s.length() == 0) {
            return "";
        }

        // Allocates a DP matrix
        int len = s.length();
        String[][] dp = new String[len][len];

        // Gets all substrings
        for (int subLen = 0; subLen < len; subLen++) {
            for (int left = 0; left + subLen < len; left++) {
                int right = left + subLen;

                // subStr is from <left> to <right>, saves it to DP matrix
                String subStr = s.substring(left, right + 1);
                dp[left][right] = subStr;

                // Checks for a shorter combination
                for (int middle = left; middle < right; middle++) {
                    String leftPart = dp[left][middle];
                    String rightPart = dp[middle + 1][right];
                    if (leftPart.length() + rightPart.length() < dp[left][right].length()) {
                        dp[left][right] = leftPart + rightPart;
                    }
                }

                // Checks for repeat substrings
                for (int middle = left; middle < right; middle++) {
                    String repeatStr = s.substring(left, middle + 1);
                    if (isRepeatedBy(subStr, repeatStr)) {
                        int repeatTimes = subStr.length() / repeatStr.length();
                        String newStr = repeatTimes + "[" + dp[left][middle] + "]";
                        if (newStr.length() < dp[left][right].length()) {
                            dp[left][right] = newStr;
                        }
                    }
                }

            }
        }

        return dp[0][len - 1];

    }

    private boolean isRepeatedBy(String subStr, String repeatStr) {
        return (subStr.length() % repeatStr.length() == 0)
            && (subStr.replaceAll(repeatStr, "").length() == 0);
    }

}
