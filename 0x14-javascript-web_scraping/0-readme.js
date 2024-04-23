#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

// console.log(argv[2])

fs.readFile(argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});
