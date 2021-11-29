function mySort(nums) {
    let evens = [];
    let odds = [];
  
    for (let i = 0; i < nums.length; i++) {
      if(typeof nums[i] === "number"){ // ignore if its not a number
        if ((nums[i] % 2) === 1) {
            odds.push(parseInt(nums[i]));
        }
        else {
            evens.push(parseInt(nums[i]));
        }
      }
    }
    let numsArray = odds.sort((a, b) => a - b).concat(evens.sort((a, b) => a - b));
    return numsArray;
  }
