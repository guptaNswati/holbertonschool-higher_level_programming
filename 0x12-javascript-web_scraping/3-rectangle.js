#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
    this.print = function () {
      for (let i = 0; i < h; i++) {
        let rectPrint = '';
        for (let j = 0; j < w; j++) {
          rectPrint += 'X';
        }
        console.log(rectPrint);
      }
    };
  }
};
