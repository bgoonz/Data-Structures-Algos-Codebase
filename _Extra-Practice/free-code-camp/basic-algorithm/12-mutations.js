function mutation( arr ) {
  const str1 = arr[ 0 ].toLowerCase();
  const str2 = arr[ 1 ].toLowerCase();
  //return arr1;

  for ( let i = 0; i < str2.length; i++ ) {
    if ( str1.indexOf( str2[ i ] ) == -1 ) {
      return false;
    }
  }
  return true;
}
console.log( mutation( [ "hello", "hey" ] ) );
