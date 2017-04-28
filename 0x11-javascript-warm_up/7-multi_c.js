#!/usr/bin/node
let myVar = process.argv.slice(2);
if (isNaN(myVar[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myVar[0]; i++) {
    console.log('C is fun');
  }
}
