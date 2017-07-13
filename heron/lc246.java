public class Solution {
    public boolean isStrobogrammatic(String num) {

        Map<Character, Character> map = new HashMap<>();
        map.put('6', '9');
        map.put('9', '6');
        map.put('8', '8');
        map.put('0', '0');
        map.put('1', '1');
        Stack<Character> stack = new Stack<>();
        for (Character c : num.toCharArray()) {
            stack.push(c);
            System.out.println("" + c);
        }
        for (Character c : num.toCharArray()) {
            char sc = stack.pop();
            System.out.println("" + c + ", " + sc);
            if (!map.containsKey(c) || map.get(c) != sc) {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
