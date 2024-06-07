
// https://leetcode.com/problems/replace-words/?envType=daily-question&envId=2024-06-07
class Solution {

    public boolean isDerivatives(String root, String derivatives) {
        if (root.length() > derivatives.length()) {
            return false;
        }
        int endIndex = root.length() - 1;
        for (int i = endIndex; i >= 0; i--) {
            if (derivatives.charAt(i) != root.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        String[] words = sentence.split(" ");
        String res = "";
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            String candidate = "";
            int candidateLength = 9999;
            int hasRoot = 0;
            for (String root : dictionary) {
                if (isDerivatives(root, word) && root.length() < candidateLength) {
                    candidate = root;
                    candidateLength = root.length();
                    hasRoot = 1;
                }
            }
            if (hasRoot == 1) {
                words[i] = candidate;
            }
        }

        for (int i = 0; i < words.length; i++) {
            if (i != words.length - 1) {
                res += words[i] + " ";
            } else {
                res += words[i];
            }
        }
        return res;

    }
}