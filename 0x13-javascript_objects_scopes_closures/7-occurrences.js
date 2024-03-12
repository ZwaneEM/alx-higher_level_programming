#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let occurences = 0;

  for (let i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      occurences += 1;
    }
  }
  return (occurences);
};
