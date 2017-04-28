#!/usr/bin/node

function secondMax (arr) {
  let currentMax = arr[0];
  let maxSoFar = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (currentMax > maxSoFar) {
      let temp = maxSoFar;
      maxSoFar = currentMax;
      currentMax = temp;
    }
    if (arr[i] > currentMax) {
      currentMax = arr[i];
    }
  }
  if (currentMax < maxSoFar) {
    console.log(currentMax);
  } else {
    console.log(maxSoFar);
  }
}

let myVar = process.argv.slice(2);
if (myVar.length > 1) {
  secondMax(myVar);
} else {
  console.log('0');
}
