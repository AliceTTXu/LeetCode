public class Solution {
    public String decodeString(String s) {
        
        // reference: https://discuss.leetcode.com/topic/57159/simple-java-solution-using-stack
        
        String result = "";
        Stack<Integer> counts = new Stack<>();
        Stack<String> buffers = new Stack<>();
        
        // start walking through the whole string
        int idx = 0;
        while (idx < s.length()) {
            if (Character.isDigit(s.charAt(idx))) {
                // retrieve the repeat number
                int c = 0;
                while (Character.isDigit(s.charAt(idx))) {
                    c = c * 10 + (s.charAt(idx) - '0');
                    idx++;
                }
                counts.push(c);
            } else if (s.charAt(idx) == '[') {
                // start a new buffer layer
                buffers.push(result);
                result = "";
                idx ++;
            } else if (s.charAt(idx) == ']') {
                // finish a buffer layer, append the result
                int c = counts.pop();
                StringBuilder sb = new StringBuilder(buffers.pop());
                for (int i=0; i<c; i++) {
                    sb.append(result);
                }
                result = sb.toString();
                idx ++;
            } else {
                // new char for buffer
                result += s.charAt(idx);
                idx ++;
            }
        }
        
        return result;
        
    }
}
