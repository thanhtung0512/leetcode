// https://leetcode.com/problems/two-sum-less-than-k/?envType=study-plan-v2&envId=binary-search
class Solution {
    public int binarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid = left + (right - left) / 2;
        while (nums[mid] != target) {
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            }
            if (left > right)
                return -1;
            mid = left + (right - left) / 2;

        }
        return mid;
    }

    public int getMin(int[] nums) {
        int minn = 999999;
        for (int x : nums) {
            if (x < minn) {
                minn = x;
            }
        }
        return minn;
    }

    public int twoSumLessThanK(int[] nums, int k) {
        Arrays.sort(nums);
        int result = -1;
        int minn = getMin(nums);
        for (int i = k - 1; i >= minn; i--) {
            for (int j = 0; j < nums.length; j++) {
                int findIndex = binarySearch(nums, i - nums[j]);
                if (findIndex != -1 && findIndex != j) {
                    System.out.println("Sum:" + i + " " + nums[j] + " " + (i - nums[j]) + '\n');
                    result = Math.max(result, i);
                }
            }
        }
        return result;
    }
}