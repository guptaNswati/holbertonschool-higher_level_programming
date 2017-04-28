#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(Number(a) + Number(b));
  }
}

let myVar = process.argv.slice(2);
if (myVar.length === 2) {
  add(myVar[0], myVar[1]);
} else {
  console.log('NaN');
}
