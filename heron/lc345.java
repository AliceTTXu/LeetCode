public class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        Stack<Character> vowels = new Stack<>();
        for (char c : chars) {
            if (isVowel(c)) {
                vowels.push(c);
            }
        }
        for (int i = 0; i < chars.length; i++) {
            if (isVowel(chars[i])) {
                chars[i] = vowels.pop();
            }
        }
        return new String(chars);
    }
    private boolean isVowel(char c) {
        char cl = Character.toLowerCase(c);
        return cl == 'a' || cl == 'e' || cl == 'i' || cl == 'o' || cl == 'u';
    }
}
