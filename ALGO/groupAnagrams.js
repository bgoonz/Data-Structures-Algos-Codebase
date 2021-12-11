/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
*/

var groupAnagrams = function(strs) {
    let map = new Map();
    for (let str of strs) {
        const s = uniform(str);
        let l = map.get(s) || [];
        l.push(str);
        map.set(s, l);
    }
    return Array.from(map.values());
};

var uniform = function(str) {
    return str.split("").sort().join(""); // /[^A-Za-z0-9]/g; // or var re = /[\W_]/g;
};

const strs = ["eat","tea","tan","ate","nat","bat"]
console.log(groupAnagrams(strs));