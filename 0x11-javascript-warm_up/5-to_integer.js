#!/usr/bin/node
let myVar = process.argv.slice(2);
if (isNaN(myVar[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar[0]);
}
