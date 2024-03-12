class Solution {
    public int search(int[] nums, int target) {
        int first = 0;
        int last = nums.length - 1;
        int mid = first + (last - first) / 2;
        while (nums[mid] != target) {

            if (nums[mid] > target) {
                last = mid - 1;

            } else if (nums[mid] < target) {
                first = mid + 1;

            }
            if (last < first) {
                return -1;
            }
            mid = first + (last - first) / 2;
        }
        if (mid >= 0 && mid <= nums.length) {
            return mid;
        } else
            return -1;
    }
}