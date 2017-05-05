#!/usr/bin/node

let fs = require('fs');
let request = require('request');
request(process.argv[2], 'utf-8', function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', function (err, data) {
    if (err) {
      console.log(err);
    }
  });
});
