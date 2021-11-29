'use strict';
/*
 * Create the function to find the factorial of a given integer
 */

function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
