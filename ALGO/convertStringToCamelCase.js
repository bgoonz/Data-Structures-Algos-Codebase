//Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
//The first word within the output should be capitalized only if the original word was capitalized.

function toCamelCase(str){
	var regex = /[-_]\w/ig;
  
  // Whenever the values in the regex variable "-_" is found in str, change the next character to an uppercase value
	return str.replace(regex,function(x){return x.charAt(1).toUpperCase()}); 
}
