// eslint-disable-next-line no-unused-vars
const ac = require('../../js/aocCommon');

// main - part 1

const getManhattanDistanceTo = (n) => {
  if (n <= 0) {
    return -1;
  }

  if (n === 1) {
    return 0;
  }
  let sz = 1;
  let start = 1;
  let end = 1;
  let found = false;
  while (!found) {
    sz += 2;
    const perimeter = (4 * sz) - 4;
    start = end + 1;
    end += perimeter;
    if (n >= start && n <= end) {
      found = true;
    }
  }
  let x = sz - 1;
  let y = sz - 1;
  const midX = Math.floor(sz / 2);
  const midY = midX;
  let num = end;
  const arr1 = Array(sz);
  for (let i = 0; i < sz; i += 1) {
    arr1[i] = ' ';
  }

  const arr = Array(sz);
  for (let i = 0; i < sz; i += 1) {
    arr[i] = [...arr1];
  }

  for (let j = 0; j < sz; j += 1) {
    arr[y][x] = num;
    if (num === n) {
      return (Math.abs(y - midY) + Math.abs(x - midX));
    }
    num -= 1;
    x -= 1;
  }

  x = 0;
  y = sz - 2;
  for (let j = 1; j < sz; j += 1) {
    arr[y][x] = num;
    if (num === n) {
      return (Math.abs(y - midY) + Math.abs(x - midX));
    }
    num -= 1;
    y -= 1;
  }

  y = 0;
  x = 1;
  for (let j = 1; j < sz; j += 1) {
    arr[y][x] = num;
    if (num === n) {
      return (Math.abs(y - midY) + Math.abs(x - midX));
    }
    num -= 1;
    x += 1;
  }

  y = 1;
  x = sz - 1;
  for (let j = 1; j < sz - 1; j += 1) {
    arr[y][x] = num;
    if (num === n) {
      return (Math.abs(y - midY) + Math.abs(x - midX));
    }
    num -= 1;
    y += 1;
  }

  return -1; // should never get here
};

const go = async () => {
  const startTime = Date.now();

  console.log(getManhattanDistanceTo(368078));

  const endTime = Date.now();
  console.log(`elapsed time: ${(endTime - startTime) / 1000.0}`);
};

go();
