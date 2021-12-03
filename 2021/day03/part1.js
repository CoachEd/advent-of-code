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

const displayPart1 = (gamma, epsilon) => {
  console.log(gamma * epsilon);
}

(async() => {
  let arr = await getData('inp.txt');
  let obj = getGammaEpsilon(arr);
  displayPart1(obj.gamma, obj.epsilon);
})();