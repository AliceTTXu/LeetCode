public class Solution {
    public String longestCommonPrefix(String[] strs) {
        String result = "";
        if (strs == null || strs.length == 0) {
            return result;
        }
        for (int i=0; i < strs[0].length(); i++) {
            char ch = strs[0].charAt(i);
            boolean isEnd = false;
            for (int j=1; j < strs.length; j++) {
                String s = strs[j];
                if (i >= s.length() || s.charAt(i) != ch) {
                    isEnd = true;
                }
            }
            if(!isEnd) {
                result += ch;
            } else {
                break;
            }
        }
        return result;
    }
}
