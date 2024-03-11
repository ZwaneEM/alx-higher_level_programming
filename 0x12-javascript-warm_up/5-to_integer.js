#!/usr/bin/node

/* prints a converted string to integer */

const args = process.argv.slice(2);
const NewInteger = parseInt(args[0]);

if (isNaN(NewInteger)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + NewInteger);
}
