#!/usr/bin/node

function secondMax (arr) {
  let maxSoFar = arr[0];
  let currentMax = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (maxSoFar < arr[i]) {
      currentMax = maxSoFar;
      maxSoFar = arr[i];
    }
  }
  console.log(currentMax);
}

let myVar = process.argv.slice(2);
if (myVar.length > 1) {
  secondMax(myVar);
} else {
  console.log(0);
}
