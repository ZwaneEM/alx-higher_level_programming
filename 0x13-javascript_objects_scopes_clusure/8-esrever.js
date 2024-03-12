#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const NewList = [];

  for (let i = len - 1; i >= 0; i--) {
    NewList.push(list[i]);
  }
  return (NewList);
};
