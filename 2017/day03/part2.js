/* eslint-disable no-constant-condition */
// eslint-disable-next-line no-unused-vars
const ac = require('../../js/aocCommon');

// main - part 2

const sumOfNeighbors = (y, x, arr) => {
  const nbrs = [[y - 1, x], [y + 1, x], [y, x - 1],
    [y, x + 1], [y + 1, x + 1], [y - 1, x + 1], [y + 1, x - 1], [y - 1, x - 1]];
  let sum = 0;
  for (let i = 0; i < nbrs.length; i += 1) {
    const ty = nbrs[i][0];
    const tx = nbrs[i][1];
    if (ty >= 0 && ty < arr.length && tx >= 0 && tx < arr.length) {
      const elem = arr[ty][tx];
      if (elem > 0) {
        sum += elem;
      }
    }
  }
  return sum;
};

const getFirstValueLargerThan = (n) => {
  const sz = 1000;
  const midX = Math.floor(sz / 2);
  const midY = midX;

  const arr1 = Array(sz);
  for (let i = 0; i < sz; i += 1) {
    arr1[i] = -1;
  }
  const arr = Array(sz);
  for (let i = 0; i < sz; i += 1) {
    arr[i] = [...arr1];
  }

  const found = false;
  let y = midY;
  let x = midX + 1;
  arr[y][x] = 1;
  while (!found) {
    // go up until left is open
    while (true) {
      y -= 1;
      const sum = sumOfNeighbors(y, x, arr);
      if (sum > n) {
        return sum;
      }
      arr[y][x] = sum;
      if (arr[y][x - 1] === -1) {
        break;
      }
    }

    // go left until down is open
    while (true) {
      x -= 1;
      const sum = sumOfNeighbors(y, x, arr);
      if (sum > n) {
        return sum;
      }
      arr[y][x] = sum;
      if (arr[y + 1][x] === -1) {
        break;
      }
    }

    // go down until right is open
    while (true) {
      y += 1;
      const sum = sumOfNeighbors(y, x, arr);
      if (sum > n) {
        return sum;
      }
      arr[y][x] = sum;
      if (arr[y][x + 1] === -1) {
        break;
      }
    }

    // go right until up is open
    while (true) {
      x += 1;
      const sum = sumOfNeighbors(y, x, arr);
      if (sum > n) {
        return sum;
      }
      arr[y][x] = sum;
      if (arr[y - 1][x] === -1) {
        break;
      }
    }
  }

  return -1;
};

const go = async () => {
  const startTime = Date.now();

  console.log(getFirstValueLargerThan(368078));

  const endTime = Date.now();
  console.log(`elapsed time: ${(endTime - startTime) / 1000.0}`);
};

go();
