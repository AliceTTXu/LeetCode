public class Solution {
    public List<String> generateAbbreviations(String word) {

        List<String> res = new ArrayList<>();
        int len = word.length();

        // Saves the corner case
        res.add(len == 0 ? "" : String.valueOf(len));

        // Lists all the possibilities
        for (int i = 0; i < len ; i++) {
            String left = (i == 0) ? "" : String.valueOf(i);
            for (String right : generateAbbreviations(word.substring(i + 1))) {
                res.add(left + word.substring(i, i + 1) + right);
            }
        }

        return res;

    }
}
