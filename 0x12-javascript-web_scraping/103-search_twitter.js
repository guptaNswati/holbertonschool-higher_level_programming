#!/usr/bin/node

let request = require('request');
let base64 = require('base-64');
let utf8 = require('utf8');

let arg = process.argv[4];
arg = arg.slice(0, 0) + arg.slice(1, arg.length);

let url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23' + arg;

let oauth = process.argv[2] + ':' + process.argv[3];
oauth = utf8.encode(oauth);
oauth = base64.encode(oauth);
oauth = utf8.decode(oauth);

let header = {
  'Authorization': 'Basic ' + oauth,
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
};

let data = {
  'grant_type': 'client_credentials'
};

let tokens = {
  url: 'https://api.twitter.com/oauth2/token',
  headers: header,
  form: data
};

request.post(tokens, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let data = JSON.parse(body);
  let access = data['access_token'];
  let searchHead = {
    'Authorization': 'Bearer ' + access
  };
  request.get({url: url, headers: searchHead}, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    let hashTags = JSON.parse(body)['statuses'];
    for (let i = 0; i < 5; i++) {
      console.log('[' + hashTags[i]['id_str'] + '] ' + hashTags[i]['text'] +
        ' by ' + hashTags[i]['user']['name']);
    }
  });
});
