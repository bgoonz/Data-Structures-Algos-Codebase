/*
Given the root of a binary tree, return the inorder traversal of its nodes' values.
 
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:
Input: root = []
Output: []
Example 3:
Input: root = [1]
Output: [1]
Example 4:
Input: root = [1,2]
Output: [2,1]
Example 5:
Input: root = [1,null,2]
Output: [1,2]
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
 var inorderTraversal = function(root) {
    // recursive method 
    let res = [];
    const inOrder = (root) => {
        if (root == null) return;
        inOrder(root.left);
        res.push(root.val);
        inOrder(root.right);
    }
    inOrder(root);
    return res;

    // iterative method
    // const stack = [], result = [];
    // root && stack.push(root);
    
    // while (stack.length) {
    //     const item = stack.pop();
    //     if (item.left) {
    //         stack.push(item);
    //         stack.push(item.left);
    //         item.left = null;
    //     }
    //     else {
    //         result.push(item.val);
    //         item.right && stack.push(item.right);
    //     }
    // }
    
    // return result;
};

const root = [1,null,2];
console.log(inorderTraversal(root))