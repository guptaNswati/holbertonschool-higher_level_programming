#!/usr/bin/node
let myVar = process.argv.slice(2);
let argLen = myVar.length;
if (argLen === 0) {
  console.log('No argument');
} else if (argLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
