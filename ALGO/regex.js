//Complete the function in the editor below by returning a RegExp object, , 
//that matches any string  that begins and ends with the same vowel. Recall that the English vowels are a, e, i, o, and u.

'use strict';


function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    const re = /^([aeiou]).*\1$/;

    /*
     * Do not remove the return statement
     */
    return re;
}

