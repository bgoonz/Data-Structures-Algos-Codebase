/* 
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
*/

const reverseWords = (s) => {
    s = s.trim();
    s = s.split(' ');
    
    let reversedArray = [];
    for (let i = s.length - 1; i >= 0; i--) {
        reversedArray.push(s[i]);
    }
    
    const indexToRemove = [];
    for (let i = 0; i < reversedArray.length; i++) {
        if (reversedArray[i] === '') {
            indexToRemove.push(i);
        }
    }
    
    for (let i = indexToRemove.length - 1; i >= 0; i--) {
        reversedArray.splice(indexToRemove[i], 1);
    }
    
    console.log(reversedArray.join(' '));
    return reversedArray.join(' ');
};

const s = "Alice does not even like bob";
reverseWords(s);