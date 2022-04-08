const ac = require('../../js/aocCommon');

// main - part 1

const go = async () => {
  const startTime = Date.now();
  const sarr = await ac.getInputArray('inp.txt');
  console.log(sarr);

  const endTime = Date.now();
  console.log(`elapsed time: ${(endTime - startTime) / 1000.0}`);
};

go();
