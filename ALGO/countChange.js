function countChange (target, arr) {
    if (target <= 0)
      return 0;

    if (!arr) {
      arr = [];
      for (var i = 1; i <= target; i++)
        arr[i] = i;
    }

    var a = []
      , b = [];

    for (var i = 0; i <= target; i++)
      a[i] = b[i] = 0;

    // start
    a[0] = 1;

    for (var i = 0; i < arr.length; i++) {

      for (var j = 0; j <= target; j++)
        for (var k = 0; j + k <= target; k += arr[i])
          b[j + k] += a[j];

      for (var j = 0; j <= target; j++)
        a[j] = b[j], b[j] = 0;
    }

    return a[target];
  }
