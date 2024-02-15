#!/usr/bin/node
const {argv} = require('process');
const argc = argv.length - 2;
if (argc == 0){
    console.log('No argument');
}else {
    console.log(`${argv[2]}`);
}

