#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  let result = JSON.parse(body);
  result = result?.results;
  const sum = 0;
  //   for (const i in result) {
  //     const comp = result[i].characters;
  //     for (const x in comp) {
  //       if (comp[x] == 'https://swapi-api.alx-tools.com/api/people/18/') {
  //         sum += 1;
  //       }
  //     }
  //   }
  console.log(result);
});