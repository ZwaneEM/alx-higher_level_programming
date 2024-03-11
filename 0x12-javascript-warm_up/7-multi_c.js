#!/usr/bin/node

/* script that prints x times c is fun */

const args = process.argv.slice(2);
const multiplier = parseInt(args[0]);

if (isNaN(multiplier)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < multiplier; i++) {
    console.log('C is fun');
  }
}
