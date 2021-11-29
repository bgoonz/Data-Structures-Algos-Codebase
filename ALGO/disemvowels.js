//Your task is to write a function that takes a string and return a new string with all vowels removed.
//
//For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
//
//Note: for this kata y isn't considered a vowel.

function disemvowel(str) {
let vowels = ['a', 'e', 'i', 'o', 'u'];
  return str.split('').filter(function(el) { 
  return vowels.indexOf(el.toLowerCase()) == -1;
  }).join('');
}