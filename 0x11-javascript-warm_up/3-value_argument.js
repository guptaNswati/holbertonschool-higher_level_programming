#!/usr/bin/node
let myVar = process.argv.slice(2);
if (myVar[0] === undefined) {
  console.log('No argument');
} else {
  console.log(myVar[0]);
}
