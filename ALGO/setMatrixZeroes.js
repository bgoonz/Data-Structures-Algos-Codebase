/*
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
*/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
 var setZeroes = function(matrix) {
    const indexToReplace = [];
    const rowToReplace = [];
    for (let i = 0; i < matrix.length; i++) {
        const row = matrix[i];
        for (let j = 0; j < row.length; j++) {
            if (row[j] === 0) {
                indexToReplace.push(j);
            }
        }
        if (row.includes(0)) {
            rowToReplace.push(i);
        }
    }
    
    
    for (let z = 0; z < rowToReplace.length; z++) {
        const row = matrix[rowToReplace[z]];
        for (let k = 0; k<row.length; k++) {
            row[k] = 0;
        } 
    }
    
    for (let z = 0; z < indexToReplace.length; z++) {
        for (let i = 0; i < matrix.length; i++) {
            const row = matrix[i];
            
            for (let j = 0; j < row.length; j++) {
                if (j === indexToReplace[z]) {
                    row[j] = 0;
                }
            }
        }
    }
};

const matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]];
setZeroes(matrix);