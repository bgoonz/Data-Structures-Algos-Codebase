// Truncate a String

/*
Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a ... ending.
*/

function truncateString(str, num) {

  if (str.length > num) {
    str = `${str.slice(0, num)}...`;
    // .substr() can be alternatively used
  }
  return str;
}

truncateString('A-tisket a-tasket A green and yellow basket', 8);
