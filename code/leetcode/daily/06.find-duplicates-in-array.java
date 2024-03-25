// https://leetcode.com/problems/find-all-duplicates-in-an-array
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int n = nums.length;
        int[] result = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            result[i] = 0;
        }
        for (int x : nums) {
            result[x]++;
        }
        List<Integer> duplicates = new ArrayList<Integer>();
        for (int i = 0; i < n + 1; i++) {
            if (result[i] == 2) {
                duplicates.add(i);
            }
        }
        return duplicates;
    }
}