#!/usr/bin/node
let request = require('request');
if (process.argv[2] !== undefined) {
  request('http://swapi.co/api/people/18', function (error, response, body) {
    if (error) {
      console.log(error);
    }
    let allData = JSON.parse(body);
    console.log(allData['films'].length);
  });
} else {
  console.log('Error: Pass the url');
}
