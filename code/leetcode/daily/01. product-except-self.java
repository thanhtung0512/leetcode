// https://leetcode.com/problems/product-of-array-except-self
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int productAll = 1;
        int numsZeros = 0;
        for (int x : nums) {
            if (x != 0) {
                productAll *= x;
            } else
                numsZeros++;

        }
        int[] result = new int[nums.length];
        for (int i = 0; i < result.length; i++) {
            if (nums[i] != 0) {
                if (numsZeros > 0) {
                    result[i] = 0;
                } else if (numsZeros == 0) {
                    result[i] = productAll / nums[i];
                }
            } else {
                if (numsZeros == 1) {
                    result[i] = productAll;
                } else if (numsZeros == 0) {
                    result[i] = productAll / nums[i];
                }
            }
        }


        
        return result;
    }
}