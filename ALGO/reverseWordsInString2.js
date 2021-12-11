/*
Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.
 
Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:
Input: s = ["a"]
Output: ["a"]
 
Constraints:
1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
*/

const reverseWords = (s) => {
    const words = [];
    const reversedWords = [];
    let currentWord = '';
    for (let i = 0; i < s.length; i++) {
        
        if (s[i] != ' ') {
            currentWord = currentWord + s[i];
        } else {
            words.push(currentWord);
            currentWord = '';
        }
        
        if (i === s.length - 1) {
            words.push(currentWord);
            currentWord = '';
        }
    }
    
    if (words.length > 0) {
        for (let i = words.length - 1; i >= 0; i--) {
            reversedWords.push(words[i]);
        }   
    }
    
    const result = reversedWords.join(' ').split('');
    
    for (let i = 0; i < result.length; i++) {
        s[i] = result[i];
    }

    console.log(s);

    return s;
};

const s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"];
reverseWords(s);