#!/usr/bin/node

/* prints the first argument passed */

const args = process.argv.slice(2);
const argsLength = args.length;

if (argsLength === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
