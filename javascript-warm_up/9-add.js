#!/usr/bin/node

/* Analysis of string that is done in argument */
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
/* if b is not a number, print 'Missin...' */
if (isNaN(b) || isNaN(a)) {
  console.log('NaN');
} else {
  function add (a, b) {
    let res = 0;
    res = a + b;
    console.log(res);
  }
  console.log(add(a, b));
}
