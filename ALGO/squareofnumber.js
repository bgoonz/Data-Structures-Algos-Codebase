// Complete the square sum method so that it squares each number passed into it and then sums the results together.

function squareSum(numbers){
  const sumSquare = numbers.map(x => x * x).reduce(function(result, item) {
    return result + item;
  }, 0);
  return sumSquare;
}