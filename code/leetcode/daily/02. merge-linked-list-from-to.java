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

//  https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        int i = 0;
        ListNode start = list1;
        ListNode end = list1;
        while (i != b) {
            end = end.next;
            i++;
        }
        i = 0;
        while (i != a - 1) {
            start = start.next;
            i++;
        }
        start.next = list2;
        ListNode iter2 = list2;
        while (iter2.next != null) {
            iter2 = iter2.next;
        }
        iter2.next = end.next;
        return list1;

    }
}