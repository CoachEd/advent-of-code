const fs = require('fs');
const readline = require('readline');

const getData = async (filename) => {
  const fileStream = fs.createReadStream(filename);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });
  let arr = [];
  for await (const line of rl) {
    arr.push(line);
  }
  return arr;
};

const makeInts = (arr) => {
  return arr.map(s => parseInt(s));
};

const increaseArr = (arr) => {
  let arrtemp = [0];
  for (let i=1; i < arr.length; i++) {
    if (arr[i] > arr[i-1])
      arrtemp.push(1);
    else
      arrtemp.push(0);
  }
  return arrtemp;
}

const add = (accumulator, a) => accumulator + a;

const calcAnswer = (arr) => arr.reduce(add, 0);

(async() => {
  let arr2, answer;
  arr2 = await getData('inp.txt');
  arr2 = makeInts(arr2);
  arr2 = increaseArr(arr2);
  answer = calcAnswer(arr2);
  console.log(answer);
})();
