#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    const hextodec = number.toString(base);
    return (hextodec);
  };
};
