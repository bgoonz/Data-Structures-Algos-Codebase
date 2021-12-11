/*
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 
Follow up: Could you solve it without reversing the input lists?
*/


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 var addTwoNumbers = function(l1, l2) {
    // make 2 stack
    let s1 = []
    let s2 = []
    
    while (l1) {
        s1.push(l1.val)
        l1 = l1.next
    }
    while (l2) {
        s2.push(l2.val)
        l2 = l2.next
    }
    
	// similiar to 2. Add Two Numbers
    let list = new ListNode(0)
    let sum = 0;
    
    while (s1.length !== 0 || s2.length !== 0 || sum > 0){
        sum = sum + (s1.length === 0? 0: s1.pop())
        sum = sum + (s2.length === 0? 0: s2.pop())
        
        // start to deal with linked list
		// update current node value
        list.val = sum % 10
        
		// add new head node with carry, head.val could be 1 or 0
		sum = Math.floor(sum/10);
        let head = new ListNode(sum)
        
		// connect
        head.next = list
        
		// update the head
        list = head
    }
    
    if (list.val === 0){
        return list.next
    } else {
        return list
    }
};

const l1 = [7,2,4,3], l2 = [5,6,4];
console.log(addTwoNumbers(l1, l2));