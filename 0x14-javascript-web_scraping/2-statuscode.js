#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
request(argv[2], (response) => {
  console.log('code: ', response && response.statusCode);
  return;
});
