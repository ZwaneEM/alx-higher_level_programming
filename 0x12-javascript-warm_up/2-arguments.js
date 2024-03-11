#!/usr/bin/node

/* Prints a message depending of the number of arguments */

const args = process.argv.slice(2);
const argsLength = args.length;

if (argsLength === 0) {
  console.log('No argument');
} else if (argsLength === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
