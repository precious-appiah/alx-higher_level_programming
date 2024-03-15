#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width = null;
      this.heigth = null;
    } else {
      this.width = w;
      this.heigth = h;
    }
  }
}
