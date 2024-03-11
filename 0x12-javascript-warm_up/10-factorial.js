#!/usr/bin/node

/* Prints a factorial of n recusively */

function factorial (NumberMod) {
  if (NumberMod === 1) {
    return (1);
  } else {
    return (NumberMod * factorial(NumberMod - 1));
  }
}

const args = process.argv.slice(2);
const ArgValue = parseInt(args[0]);

if (isNaN(ArgValue)) {
  console.log(1);
} else {
  console.log(factorial(ArgValue));
}
