#!/usr/bin/node
exports.esrever = function (list) {
  const newArr = [];
  let i = list.length - 1;
  while (i >= 0) {
    newArr.push(list[i]);
    i--;
  }
  return newArr;
};
