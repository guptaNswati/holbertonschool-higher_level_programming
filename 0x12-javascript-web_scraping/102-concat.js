#!/usr/bin/node

let fs = require('fs');
let fileData = '';

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
  fileData += data;
  fs.readFile(process.argv[3], 'utf-8', function (err, data) {
    if (err) {
      console.log(err);
    }
    fileData += data;
    fs.writeFile(process.argv[4], fileData, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  });
});
