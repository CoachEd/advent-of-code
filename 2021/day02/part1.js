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

const makeObj = (s) => {
  let arr = s.split(' ');
  return { cmd: arr[0], x: parseInt(arr[1]) };
}

const objArr = (arr) => arr.map(s => makeObj(s));

const getDepthHoriz = (arr) => {
  let depth = 0;
  let horiz = 0;
  for (let i=0; i < arr.length; i++) {
    let obj = arr[i];
    if (obj.cmd == 'forward')
      horiz += obj.x;
    else if (obj.cmd == 'down')
      depth += obj.x;
    else
      depth -= obj.x;
  }
  return { depth, horiz };
}

const dispAnswer = (depth, horiz) => {
  console.log(depth * horiz);
}

(async() => {
  let arr2 = await getData('inp.txt');
  arr2 = objArr(arr2);
  let obj = getDepthHoriz(arr2);
  dispAnswer(obj.depth, obj.horiz);
})();
