#!/usr/bin/node

/* prints a square */

const args = process.argv.slice(2);
const NewInteger = parseInt(args[0]);
let x;
let i;

if (isNaN(NewInteger)) {
  console.log('Missing size');
} else {
  for (i = 0; i < NewInteger; i++) {
    for (x = 0; x < NewInteger; x++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
