/*
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
 
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:
Input: nums = [0]
Output: [0]
Example 4:
Input: nums = [1]
Output: [1]
 
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
 
Follow up: Could you come up with a one-pass algorithm using only constant extra space?
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var sortColors = function(nums) {
    let a = 0;
    let b = 0;
    let len = nums.length;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            nums[i] = 2;
            nums[b++] = 1;
            nums[a++] = 0;
        } else if (nums[i] === 1) {
            nums[i] = 2;
            nums[b++] = 1;
        } else {
            nums[i] = 2;
        }
    }
};

const nums = [2,0,2,1,1,0];
console.log(sortColors(nums));