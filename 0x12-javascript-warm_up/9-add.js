#!/usr/bin/node
const { argv } = require('process');

add(Number(argv[2]), Number(argv[3]));

function add (a, b) {
  const result = a + b;
  console.log(result);
}
