const ac = require('../../js/aocCommon');

// main - part 1

const go = async () => {
  const startTime = process.hrtime();

  const sarr = await ac.getInputArray('inp.txt');
  console.log(sarr);

  const endTime = process.hrtime();
  console.log(`elapsed time: ${((endTime[0] / 1000000000 + endTime[1]) - (startTime[0] / 1000000000 + startTime[1])) / 1000000000}`);
};

go();
