/* 
Given the head of a singly linked list, reverse the list, and return the reversed list.
 
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseListIteratively = function(head) {
     // iteratively
    if (!head){
         return head;
     }
    
     let current = head.next;
    
     let node = head;
     node.next = null;
    
     while(current){
         let temp = current;
         current = current.next
         temp.next = node;
         node = temp;
     }
    
     return node;
};

var reverseListRecursively = function(head, prev = null) {
    // recursively
    if (!head){
        return head;
    }

    const next = head.next;
    head.next = prev;

    return next ? reverseList(next, head) : head;
};