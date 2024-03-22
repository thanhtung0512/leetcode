/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// https://leetcode.com/problems/reverse-linked-list/?envType=daily-question&envId=2024-03-21
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null)
            return head;
        if (head.next == null)
            return head;
        ListNode newHead = head;
        ListNode prevLastNode = null;
        while (newHead.next != null) {
            prevLastNode = newHead;
            newHead = newHead.next;
        }
        prevLastNode.next = null;
        newHead.next = reverseList(head);
        return newHead;
    }
}