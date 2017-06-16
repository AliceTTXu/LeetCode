public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<>();
        if (num == null || num.length() == 0) {
            return result;
        }
        helper(result, num, target, "", 0, 0, 0);
        return result;
    }

    private void helper(List<String> result, String num, int target, String path, int pos, long eval, long holder) {

        // we've reached the end of input numbers
        if (pos == num.length()) {
            // if this eval is equal to target, save it as result
            if (eval == target) {
                result.add(path);
            }
            return;
        }

        for (int i=pos; i<num.length(); i++) {
            // not sure why this check is needed, ex:
            // 105, target: 6, 1 * 5
            if (i!=pos && num.charAt(pos) == '0') {
                break;
            }
            long cur = Long.parseLong(num.substring(pos, i+1));
            if (pos == 0) {
                helper(result, num, target, path + cur, i+1, eval + cur, cur);
            } else {
                helper(result, num, target, path + "+" + cur, i+1, eval + cur, cur);
                helper(result, num, target, path + "-" + cur, i+1, eval - cur, -cur);
                helper(result, num, target, path + "*" + cur, i+1, eval - holder + holder * cur, holder * cur);
            }
        }

    }
}
