const ac = require('../../js/aocCommon');

// main - part 2

const checkSum2 = (a) => {
  // array rows must be sorted in descending order
  let sum = 0;
  for (let i = 0; i < a.length; i += 1) {
    const a2 = a[i];
    for (let j = 0; j < a2.length - 1; j += 1) {
      for (let k = j + 1; k < a2.length; k += 1) {
        if (a2[j] % a2[k] === 0) {
          sum += a2[j] / a2[k];
        }
      }
    }
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
    arr[i] = ac.strArrToIntArr(arrTemp).sort((a, b) => b - a);
  }

  console.log(checkSum2(arr));
  const endTime = Date.now();
  console.log(`elapsed time: ${(endTime - startTime) / 1000.0}`);
};

go();
