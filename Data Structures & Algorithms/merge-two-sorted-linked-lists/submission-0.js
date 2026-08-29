/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        const prehead = new ListNode()
        let [curr, p1, p2] = [prehead, list1, list2]

        while(p1 && p2){
            if(p1.val < p2.val){
                curr.next = p1
                p1 = p1.next
            } else {
                curr.next = p2
                p2 = p2.next
            }
            curr = curr.next
        }

        curr.next = p1?p1:p2

        return prehead.next
    }
}
