#!/usr/bin/node
const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const info = JSON.parse(body);
  let tracker = 0;
  let id = 0;
  let min = 0;
  console.log(info.length);
  while (tracker < info.length) {
    let sum = 0;
    for (const i in info) {
      if (info[i].userId == id && info[i].completed == true) {
        sum++;
      }
    }
    min = sum;
    id++;
    tracker++;
  }
  // console.log(info[id - 1].userId,":", min)
});
