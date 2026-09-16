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
    public ListNode mergeKLists(ListNode[] lists) {
        ArrayList<Integer> stuff = new ArrayList<>();
        
        for (ListNode list : lists) {
            while (list != null) {
                stuff.add(list.val);
                list = list.next;
            }
        }

        Collections.sort(stuff);

        //System.out.println(stuff);

        ListNode dummy = new ListNode();
        ListNode head = dummy;
        for (int item : stuff) {
            dummy.next = new ListNode(item);
            dummy = dummy.next;
        }

        return head.next;
    }
}
