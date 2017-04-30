#!/usr/bin/node

var request = require('request');
request(process.argv[2], 'utf-8', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let data = JSON.parse(body);
  let dict = {};
  for (let i = 0; i < data.length; i++) {
    if (data[i]['completed']) {
      let key = data[i]['userId'];
      if (!(key in dict)) {
        dict[key] = 1;
      } else {
        dict[key] += 1;
      }
    }
  }
  console.log(dict);
});
