#!/usr/bin/node

function secondMax (arr) {
  let maxSoFar = Number(arr[0]);
  let currentMax = maxSoFar;
  for (let i = 1; i < arr.length; ++i) {
    let num = Number(arr[i]);
    if (num > maxSoFar) {
      currentMax = maxSoFar;
      maxSoFar = num;
    } else if (num > currentMax) {
      currentMax = num;
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
