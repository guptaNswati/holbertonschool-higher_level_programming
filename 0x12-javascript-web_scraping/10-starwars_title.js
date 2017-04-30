#!/usr/bin/node
let request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let data = JSON.parse(body);
  console.log(data['title']);
});
