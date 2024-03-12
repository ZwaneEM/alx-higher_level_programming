#!/usr/bin/node

let currentBase = 0;

exports.converter = function (base) {
  currentBase = base;
  return function (number) {
    return (number.toString(currentBase));
  };
};
