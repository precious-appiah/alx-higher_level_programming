#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const fs = require('fs');

request(`${argv[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(`${argv[3]}`, body, 'utf-8', (error) => {
    if (error) console.log(error);
  });
});
