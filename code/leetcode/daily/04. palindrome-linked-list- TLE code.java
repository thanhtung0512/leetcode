/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

//  https://leetcode.com/problems/palindrome-linked-list

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode lastNode = head;
        ListNode prevLastNode = null;
        while(lastNode.next != null ) {
            prevLastNode = lastNode;
            lastNode = lastNode.next;
        }   
        if (head == lastNode) {
            return true;
        }
        if (head.val == lastNode.val && head.next == lastNode) return true;
        if (head.val != lastNode.val) {
            return false;
        }

        prevLastNode.next = null;
        return isPalindrome(head.next);
    }
}