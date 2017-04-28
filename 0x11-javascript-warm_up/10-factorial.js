#!/usr/bin/node

function factorial (a) {
  let result = 1;
  while (a > 0) {
    result *= a;
    a--;
  }
  console.log(result);
}

let myVar = process.argv.slice(2);
if (myVar.length === 1 && !(isNaN(myVar[0]))) {
  factorial(Number(myVar[0]));
} else {
  console.log('1');
}
