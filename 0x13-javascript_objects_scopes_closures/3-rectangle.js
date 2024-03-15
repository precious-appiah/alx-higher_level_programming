#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;

    for (i = 0; i < this.height; i++) {
        let k= '';
        for (j = 1; j <= this.width; j++) {
        k = k + 'X';
      }
      console.log(k);
    }
  }
}

module.exports = Rectangle;
