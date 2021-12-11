/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true
Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
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
 * @return {boolean}
 */
 var isValidBST = function(root) {
    return validate(root, null, null);
};

var validate = function(root, low, high) {
    if (root === null) {
        return true;
    }

    if ((low != null && root.val <= low) || (high != null && root.val >= high)) {
        return false;
    }
    
    return validate(root.left, low, root.val) && validate(root.right, root.val, high);
}

const root = [5,1,4,null,null,3,6];
console.log(isValidBST(root))

// Inorder Traversal
var isValidate2 = function(root) {
    let prev = null;
    validate2(root, prev);
}

var validate2 = function(root, prev) {
    if (root === null) {
        return true;
    }

    if (!validate2(root.left)) {
        return false;
    }

    if (prev != null && root.val <= prev) {
        return false;
    }

    prev = root.val;
    return validate2(root.right)

    // Time O(n)
    // Space O(n)
}