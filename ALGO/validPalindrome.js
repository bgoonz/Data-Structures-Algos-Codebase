/*
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
*/
const s = "A man, a plan, a canal: Panama";
const isPalindrome = (s) => {
    const re = /[^A-Za-z0-9]/g; // or var re = /[\W_]/g;
    s = s.toLowerCase().replace(re, '');
    const len = s.length;
    for (let i = 0; i < len/2; i++) {
      if (s[i] !== s[len - 1 - i]) {
          return false;
      }
    }
    return true;
}

console.log(isPalindrome(s));