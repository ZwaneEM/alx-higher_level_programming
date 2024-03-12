#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let x = 0; x < this.width; x++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
}

module.exports = Rectangle;
