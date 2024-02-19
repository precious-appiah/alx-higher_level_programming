#!/usr/bin/node
const { argv } = require('process');
const n = argv[2];
let res;
function factorial (n) {
  if (!n || isNaN(Number(n)) || Number(n) === 0 || Number(n) === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
