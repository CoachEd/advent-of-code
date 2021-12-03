const fs = require('fs');
const readline = require('readline');
const internal = require('stream');

const getData = async (filename) => {
  const rl = readline.createInterface({ input: fs.createReadStream(filename), crlfDelay: Infinity });
  let arr = [];
  for await (const line of rl)
    arr.push(line);
  return arr;
};

const getCounts = (arr, pos) => {
  let obj = { ones: 0, zeros: 0 };
  arr.forEach(e => {
    if (e[pos] == '1')
      obj.ones += 1;
    else
      obj.zeros += 1;
  });
  return obj;
}

const getGammaEpsilon = (arr) => {
  let length = arr[0].length;
  let gamma = new Array(length);
  let epsilon = new Array(length);
  for (let i=0; i < length; i++) {
    let obj = getCounts(arr, i);
    gamma[i] = '0';
    epsilon[i] = '1';
    if (obj.ones > obj.zeros) {
      gamma[i] = '1';
      epsilon[i] = '0';
    }
  }
  return { gamma: parseInt(gamma.join(''), 2), epsilon: parseInt(epsilon.join(''), 2) };
}

const getOgr = (arr) => {
  let arr1 = arr.slice();
  let arr2 = [];
  let length = arr1[0].length;
  for (let i=0; i < length; i++) {
    let obj = getCounts(arr1, i);
    let c = (obj.ones >= obj.zeros) ? '1' : '0';
    arr1.forEach(s => {
      if (s[i] == c)
        arr2.push(s);
    });
    if (arr2.length == 1)
      break;
    arr1 = arr2.slice();
    arr2 = [];
  }
  return parseInt(arr2.join(''), 2);
}

const getCsr = (arr) => {
  let arr1 = arr.slice();
  let arr2 = [];
  let length = arr1[0].length;
  for (let i=0; i < length; i++) {
    let obj = getCounts(arr1, i);
    let c = (obj.zeros <= obj.ones) ? '0' : '1';
    arr1.forEach(s => {
      if (s[i] == c)
        arr2.push(s);
    });
    if (arr2.length == 1)
      break;
    arr1 = arr2.slice();
    arr2 = [];
  }
  return parseInt(arr2.join(''), 2);
}

const displayPart1 = (gamma, epsilon) => {
  console.log(gamma * epsilon);
}

const displayPart2 = (ogr, csr) => {
  console.log(ogr * csr);
}

(async() => {
  let arr = await getData('inp.txt');
  let obj = getGammaEpsilon(arr);
  displayPart1(obj.gamma, obj.epsilon);
  let ogr = getOgr(arr);
  let csr = getCsr(arr);
  displayPart2(ogr, csr);
})();