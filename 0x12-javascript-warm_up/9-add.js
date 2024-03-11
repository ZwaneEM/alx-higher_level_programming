#!/usr/bin/node

/* prints the addition of 2 integers */

function add (a, b) {
  console.log(a + b);
}

const args = process.argv.slice(2);

add(parseInt(args[0]), parseInt(args[1]));
