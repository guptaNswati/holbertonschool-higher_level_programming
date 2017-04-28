#!/usr/bin/node

let factorial = function (a) {
  if (a <= 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
};

let myVar = process.argv.slice(2);
if (myVar.length === 1 && !(isNaN(myVar[0]))) {
  console.log(factorial(Number(myVar[0])));
} else {
  console.log('1');
}
