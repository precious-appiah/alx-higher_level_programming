#!/usr/bin/node
const request = require('request');
const {argv} = require('process');
const fs = require('fs');

request(`${argv[2]}`,(error, response, body)=>{
    if(error){
        console.log(error);
        return;
    }
    console.log(argv[3])
    fs.writeFile(`${argv[3]}`,body, (error)=>{
        if(error){

            console.log('hmmmmmmmm');
            return;
        }

    })

})

