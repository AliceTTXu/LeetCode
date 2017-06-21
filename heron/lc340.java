public class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {

        // Uses to trace the number of distinct characters
        Map<Character, Integer> map = new HashMap<Character, Integer>();

        // Stores the longest substring length
        int best = 0;

        // Left index of the picked substring
        int left = 0;

        for (int i=0; i<s.length(); i++) {

            // Stores the most right character
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);

            // Deletes the most left character if needed
            while (map.size() > k) {
                char leftChar = s.charAt(left);
                if (map.containsKey(leftChar)) {
                    map.put(leftChar, map.get(leftChar)-1);
                    if (map.get(leftChar) == 0) {
                        map.remove(leftChar);
                    }
                }
                left ++;
            }

            // Stores the longest substring we've found so far with k distinct characters
            best = Math.max(best, i - left + 1);

        }

        return best;

    }
}
