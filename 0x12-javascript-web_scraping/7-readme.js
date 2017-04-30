#!/usr/bin/node

var fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
