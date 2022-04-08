const ac = require('../../js/aocCommon');

// main - part 1

const checkSum = (a) => {
  // array rows must be sorted in ascending order
  let sum = 0;
  for (let i = 0; i < a.length; i += 1) {
    sum += a[i][a[i].length - 1] - a[i][0];
  }
  return sum;
};

const go = async () => {
  const startTime = Date.now();
  const sarr = await ac.getInputArray('inp.txt');
  const arr = Array(sarr.length);
  for (let i = 0; i < arr.length; i += 1) {
    const arrTemp = sarr[i].split('\t');

    // numeric sort ascending; use b - a for descending
    arr[i] = ac.strArrToIntArr(arrTemp).sort((a, b) => a - b);
  }

  console.log(checkSum(arr));
  const endTime = Date.now();
  console.log(`elapsed time: ${(endTime - startTime) / 1000.0}`);
};

go();
