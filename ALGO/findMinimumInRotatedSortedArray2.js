/*
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
 
Example 1:
Input: nums = [1,3,5]
Output: 1
Example 2:
Input: nums = [2,2,2,0,1]
Output: 0
 
Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
 
Follow up: This is the same as Find Minimum in Rotated Sorted Array but with duplicates. Would allow duplicates affect the run-time complexity? How and why?
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMin = function(nums) {
    let min;
    
    for (let i = 0; i < nums.length; i++) {
        if (min != nums[i]) {
            if (!min && min != 0) {
                min = nums[i];
            } else {
                if (min > nums[i]) {
                    min = nums[i];
                }
            }
        }
    }
    
    return min;
};

const nums = [2,2,2,0,1];
console.log(findMin(nums));