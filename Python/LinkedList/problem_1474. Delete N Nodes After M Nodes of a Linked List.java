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

class Solution {
    public ListNode deleteNodes(ListNode head, int m, int n) {
        ListNode current = head;
        ListNode lastM = head; 
        while(current != null){
            int mCount = m, nCount = n;
            while(current != null && mCount != 0){
                lastM = current;
                current = current.next;
                mCount--;
            }
            
            while(current != null && nCount != 0){
                current = current.next;
                nCount--;
            }
            lastM.next = current;
        }
        return head;
    }
}