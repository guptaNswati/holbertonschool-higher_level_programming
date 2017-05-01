#!/usr/bin/node
let list = require('./100-data').list;
console.log(list);
list.map((value, index) => {
  list[index] = value * index;
});
console.log(list);
