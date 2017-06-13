public class Solution {
    public String licenseKeyFormatting(String S, int K) {

        // queue and length
        Queue<Character> queue = new LinkedList<>();
        int len = S.length();

        // add valid char into queue reversely
        for (int i=len-1; i>=0; i--) {
            char c = Character.toUpperCase(S.charAt(i));
            if (c != '-') {
                queue.offer(c);
            }
        }

        // build string
        StringBuilder sb = new StringBuilder();
        int count = 0;
        while(!queue.isEmpty()) {
            sb.append(queue.poll());
            count ++;
            if (count % K == 0 && !queue.isEmpty()) {
                sb.append("-");
            }
        }

        return sb.reverse().toString();

    }
}
