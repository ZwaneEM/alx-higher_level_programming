#!/usr/bin/node

/* searches for the second biggest integer in the list */

function getLargest (listArray) {
  listArray.sort((a, b) => a - b);
  return (listArray[listArray.length - 2]);
}

const args = process.argv.slice(2);
const len = args.length;
const list = [];

if (len <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < len; i++) {
    list[i] = parseInt(args[i]);
  }

  console.log(getLargest(list));
}
