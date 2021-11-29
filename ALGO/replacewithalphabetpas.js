//In this kata you are required to, given a string, replace every letter with its position in the alphabet.
//
//If anything in the text isn't a letter, ignore it and don't return it.

function alphabetPosition(text) {
  var alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
  return text.toLowerCase().replace(/[^a-z]/g,'').split('').map(x => alphabets.indexOf(x)+1).join(' ');
}