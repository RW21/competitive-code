/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    public boolean hasCycle(ListNode head) {
        // edge case
        if (head.next == null || head == null){
            return false;
        }

        ListNode current = head;
        ListNode next = head.next;

        while (next != null && current != null){
            current = current.next;
            // bad naming
            next = next.next.next;
            
            if (next == current){
                return true;
            }

        }

        return (next==current);


        
    }
}