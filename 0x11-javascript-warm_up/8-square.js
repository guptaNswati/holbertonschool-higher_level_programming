#!/usr/bin/node
let myVar = process.argv.slice(2);
if (isNaN(myVar[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar[0]; i++) {
    let square = '';
    for (let j = 0; j < myVar[0]; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
