const fs = require('fs');

const getInputString = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (!err) {
      resolve(data);
    }
    reject(new Error(`Error: ${err}`));
  });
});

const getInputArray = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (!err) {
      resolve(data.split('\n'));
    }
    reject(new Error(`Error: ${err}`));
  });
});

const strToIntArray = (s) => {
  // convert string of digits to array of ints
  // e.g. '0394' => [0, 3, 9, 4]
  if (!s) {
    return [];
  }
  const arr1 = Array(s.length);
  for (let i = 0; i < s.length; i += 1) {
    arr1[i] = parseInt(s.charAt(i), 10);
  }
  return arr1;
};

const rotRightArray = (a, n) => {
  // rotate array to the right n times
  // e.g. [0, 1, 2, 3, 4, 5], 2 => [4, 5, 0, 1, 2, 3]
  if (!a || !n || a.length === 0 || n === 0) {
    return a;
  }
  let n1 = n % a.length;
  const arr1 = Array(a.length);
  for (let i = 0; i < a.length; i += 1) {
    arr1[n1] = a[i];
    n1 += 1;
    if (n1 >= a.length) {
      n1 = 0;
    }
  }
  return arr1;
};

module.exports = {
  getInputString,
  getInputArray,
  strToIntArray,
  rotRightArray
};
