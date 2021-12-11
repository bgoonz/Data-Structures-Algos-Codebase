/*
  Amazon Logistics would like to quickly set up a roof over a parking lot. 
  There are many cars parked in the parking lot and the lot is in a straight line. There are n cars currently
  parked and a roofer needs to cover them with a roof . The requirement is that atleast k cars currently in the lot are covered
  by the roof. Determine the minimum length of the roof to cover k cars.

  Example 
  n = 4
  cars = [6,2,12,7]
  k = 3

  Two roofs that cover three cars are possible: one covering spots 2 through 7 with a length of 6, and another covering
  slots 6 through 12 with a length of 7. The shortest roof that meets the requirement is of length 6.
*/

function carParkingRoof(cars, k) {
    cars.sort((a, b) => {
        return a-b;
    });
    let length = cars.length;
    let min = cars[k-1] - cars[0] + 1;
    for (let i = 0; i < length - k + 1; i++) {
        let temp = cars[i+k-1] - cars[i];
        if (temp < min) {
            min = temp + 1
        }
    }
    return min;
}