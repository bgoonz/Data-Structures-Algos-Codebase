/*
Given a string s, return the longest palindromic substring in s.
 
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
Example 3:
Input: s = "a"
Output: "a"
Example 4:
Input: s = "ac"
Output: "a"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
*/

const longestPalindrome = function(s) {
    if (s.length <= 1) return s;
    let start = 0,
      end = 0;
    for (let i = 0; i < s.length; i++) {
      const len1 = expandAroundCenter(s, i, i);
      const len2 = expandAroundCenter(s, i, i + 1);
      const len = Math.max(len1, len2);
      if (len > end - start) {
        start = i - (len-1) / 2;
        end = i + len / 2;
      }
    }
    return s.slice(Math.ceil(start), end + 1);
};

function expandAroundCenter(s, left, right) {
    let L = left,
    R = right;
    while (L > -1 && R < s.length) {
        if (s[L] !== s[R]) break;
        L--;
        R++;
    }
    return R - L - 1;
}

const s = "abb"
console.log(longestPalindrome(s));