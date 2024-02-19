#!/usr/bin/node
const { argv } = require('process');

const size = argv[2];
let i, j;

if (Number(size)) {
  for (i = 0; i < size; i++) {
    let k = '';
    for (j = 1; j <= size; j++) {
      k = k + 'X';
    }
    console.log(k);
  }
} else {
  console.log('Missing size');
}
