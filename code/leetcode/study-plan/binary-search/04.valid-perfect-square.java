// https://leetcode.com/problems/valid-perfect-square
class Solution {
    public boolean isPerfectSquare(int num) {
        return Math.sqrt(num) == (int) Math.sqrt(num);
    }
}