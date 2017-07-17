public class Solution {

    private static final Map<Integer, String> keymap;
    static {
        Map<Integer, String> m = new HashMap<>();
        m.put(0, "");
        m.put(1, "");
        m.put(2, "abc");
        m.put(3, "def");
        m.put(4, "ghi");
        m.put(5, "jkl");
        m.put(6, "mno");
        m.put(7, "pqrs");
        m.put(8, "tuv");
        m.put(9, "wxyz");
        keymap = Collections.unmodifiableMap(m);
    }

    public List<String> letterCombinations(String digits) {

        // Initiailzes the lists
        List<String> res = new ArrayList<>();
        List<Character> buffer = new ArrayList<>();

        // Checks for invalid input
        if (digits == null || digits.length() == 0) {
            return res;
        }

        // Gets the combinations
        getCombinations(digits, res, buffer);
        return res;

    }

    private void getCombinations(String remain, List<String> res, List<Character> buffer) {

        // Saves the buffered content to result, if there's no more chars in remain
        if (remain.length() == 0) {
            saveToResult(res, buffer);
            return;
        }

        // Gets the possible letters
        int d = remain.charAt(0) - '0';
        String letters = keymap.get(d);

        // Tries all the letters
        for (char c : letters.toCharArray()) {
            buffer.add(c);
            getCombinations(remain.substring(1), res, buffer);
            buffer.remove(buffer.size() - 1);
        }

    }

    private void saveToResult(List<String> res, List<Character> buffer) {
        StringBuilder sb = new StringBuilder();
        for (char c : buffer) {
            sb.append(c);
        }
        res.add(sb.toString());
    }

}
