#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  let i = 2;
  while (i < argv.length) {
    arr.push(Number(argv[i]));
    i++;
  }
  let first = arr[0];
  let second = arr[0];
  for (let j = 0; j < arr.length; j++) {
    if (first < arr[j]) {
      second = first;
      first = arr[j];
    } else if (second < arr[j]) {
      second = arr[j];
    }
  }
  console.log(second);
}
