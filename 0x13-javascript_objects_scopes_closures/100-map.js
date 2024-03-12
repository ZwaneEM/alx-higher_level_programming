#!/usr/bin/node

const ArrayData = require('./100-data').list;

const NewArray = ArrayData.map(function (number, index) {
  return (number * index);
});

console.log(ArrayData);
console.log(NewArray);
