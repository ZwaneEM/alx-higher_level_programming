#!/usr/bin/node

const DictData = require('./101-data').dict;

const keys = Object.keys(DictData);
const values = Object.values(DictData);

const NewData = {};

values.forEach(function (value, index) {
  if (!NewData[value]) {
    NewData[value] = [];
  }

  NewData[value].push(keys[index]);
});

console.log(NewData);
