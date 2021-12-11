/*
  A special event coordinator for Amazon Web Services is planning to host a series of presenations by different companies for a Day 1
  Orientation. The coordinator has a list of companies along with their respective arrival times and their duration
  of stay. Only one company can be presentation at any time. Given each company's arrival time and the diartion they
  will stay, determine the maximum number of presentations that can be hosted during the orientation

  example 
  n = 5
  arrival = [1,3,3,5,7]
  duration = [2,2,1,2,1]

  The first company arrives at time 1 and stays for 2 hours. At time 3, two companies arrive, but only 1 can stay for either 
  1 or 2 hours. The next companies arrive at time 5 and 7 and do not conflict with any others. In total, there can be a maximum of 4
  promotional events.
*/
function maxEvents(arrival, duration) {
    let counter = 1;

    for (let i = 1; i < arrival.length; i++) {
        const tempDuration = (arrival[i - 1] + duration[i - 1]) - 1;
        if (tempDuration <= arrival[i]) {
            counter++;
        }
    }

    return counter;
}

console.log(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1])) // 4
console.log(maxEvents([1, 2], [7, 3])) // 1
console.log(maxEvents([1, 3, 4, 6], [4, 3, 3, 2])) // 2