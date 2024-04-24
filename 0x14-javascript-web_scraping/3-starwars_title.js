#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const result = JSON.parse(body);
  console.log(result.title);
});
