#!/usr/bin/node
const Square = require('./5-square').Square;
Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    this.print();
  } else {
    for (let j = 0; j < this.size; j++) {
      let squarePrint = '';
      for (let k = 0; k < this.size; k++) {
        squarePrint += c;
      }
      console.log(squarePrint);
    }
  }
};

exports.Square = Square;
