function StopWatch() {

  let startTime = null;
  let stopTime = null;
  let isRunning = false;
  let duration = 0;

 this.start = () => {
    if(isRunning) {
      console.log('running...');
      throw new Error('Stopwatch has already started')
    }
    isRunning = true;
    startTime = new Date();
    console.log('starttime', startTime)
  }
  this.stop = () => {
    if(!isRunning) {
      console.log('Not running');
      throw new Error('Stopwatch has already started')
    }
    isRunning = false;
    stopTime = new Date();
    duration = (stopTime.getTime() - startTime.getTime()) / 1000;
    console.log(duration);
  }


  this.reset = () => {
    startTime = null;
    stopTime = null;
    isRunning = false;
    duration = 0;
  }
}

const stopWatch = new StopWatch();

// console.log('func', stopWatch.start())
// console.log('func', stopWatch.stop())
// console.log('func', stopWatch.reset())
