public class Codec {

    private char SPLIT = '#';

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length()).append(SPLIT).append(s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        for (int low = 0, i = 0; i < s.length(); i++) {
            if (s.charAt(i) == SPLIT) {
                int len = Integer.parseInt(s.substring(low, i));
                res.add(s.substring(i + 1, i + 1 + len));
                low = i + 1 + len;
                i = i + 1 + len;
            }
        }
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
