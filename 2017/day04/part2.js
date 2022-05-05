// eslint-disable-next-line no-unused-vars
const ac = require('../../js/aocCommon');

// main - part 2

const arrSortedWords = (a) => {
  const finalArr = [];
  for (let i = 0; i < a.length; i += 1) {
    const tempArr = [];
    const pwd = a[i];
    const arr = pwd.split(' ');
    for (let j = 0; j < arr.length; j += 1) {
      const arr1 = [...arr[j]];
      arr1.sort();
      tempArr.push(arr1.join(''));
    }
    finalArr.push(tempArr.join(' '));
  }
  return finalArr;
};

const countValidPasswords = (a) => {
  let numValid = 0;
  for (let i = 0; i < a.length; i += 1) {
    const pwd = a[i];
    const obj = {};
    const arr = pwd.split(' ');
    let valid = true;
    for (let j = 0; j < arr.length; j += 1) {
      if (obj[arr[j]]) {
        obj[arr[j]] += 1;
      } else {
        obj[arr[j]] = 1;
      }
      if (obj[arr[j]] > 1) {
        valid = false;
        break;
      }
    }
    if (valid) {
      numValid += 1;
    }
  }
  return numValid;
};

const go = async () => {
  const startTime = Date.now();
  const sarr = await ac.getInputArray('inp.txt');
  const sarrSorted = arrSortedWords(sarr);
  console.log(countValidPasswords(sarrSorted));

  const endTime = Date.now();
  console.log(`elapsed time: ${(endTime - startTime) / 1000.0}`);
};

go();
