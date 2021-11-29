//Complete the vowelsAndConsonants function in the editor below. It has one parameter, a string, , consisting of lowercase English alphabetic letters (i.e., a through z). The function must do the following:
//
//First, print each vowel in  on a new line. The English vowels are a, e, i, o, and u, and each vowel must be printed in the same order as it appeared in .
//Second, print each consonant (i.e., non-vowel) in  on a new line in the same order as it appeared in .

'use strict';

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowel = ["a", "e", "i", "o", "u"];
    for (let v of s) {
        if (vowel.includes(v)) {
            console.log(v);
        }
    }
    for (let v of s) {
        if (!vowel.includes(v)) {
            console.log(v);
        }
    }
}