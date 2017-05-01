#!/usr/bin/node
let dict = require('./101-data').dict;
let newDict = {};

for (let key in dict) {
  let newKey = dict[key];
  if (!(newKey in newDict)) {
    newDict[newKey] = [key];
  } else {
    newDict[newKey].push(key);
  }
}
console.log(newDict);
