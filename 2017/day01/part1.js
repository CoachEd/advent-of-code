const ac = require('../../js/aocCommon');

// main
const captcha = (a) => {
  if (a && a.length > 0) {
    let total = 0;
    for (let i = 0; i < a.length - 1; i += 1) {
      if (a[i] === a[i + 1]) {
        total += a[i];
      }
    }
    if (a[a.length - 1] === a[0]) {
      total += a[a.length - 1];
    }
    return total;
  }
  return 0;
};

const go = async () => {
  const startTime = process.hrtime();

  const sarr = await ac.getInputArray('inp.txt');
  const s = sarr[0];
  const arr = ac.strToIntArray(s);
  console.log(captcha(arr));

  const endTime = process.hrtime();
  console.log(`elapsed time: ${((endTime[0] / 1000000000 + endTime[1]) - (startTime[0] / 1000000000 + startTime[1])) / 1000000000}`);
};

go();
