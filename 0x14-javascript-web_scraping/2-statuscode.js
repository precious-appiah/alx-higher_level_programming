#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
request(argv[2], (error, response) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:',response && response.statusCode);
});
