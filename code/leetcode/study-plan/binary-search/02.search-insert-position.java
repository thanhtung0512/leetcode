class Solution {
    public int searchInsert(int[] nums, int target) {
        int first = 0;
        int last = nums.length - 1;
        int mid = first + (last - first) / 2;
        while (nums[mid] != target) {
            if (nums[mid] > target) {
                last = mid - 1;
            }
            else if (nums[mid] < target) {
                first = mid + 1;
            }
            if (last < first) {
                return first;
            }
            mid = first + (last - mid) / 2;
        }
        return mid;

    }
}