#!/usr/bin/node
const { argv } = require('process');
let i = 0;

if (Number(argv[2])) {
  while (i <= Number(argv[2])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
