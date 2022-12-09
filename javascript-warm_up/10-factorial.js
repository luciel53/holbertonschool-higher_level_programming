#!/usr/bin/node
/* Analysis of string that is done in argument */
const a = parseInt(process.argv[2]);
/* if b is not a number, print 'Missin...' */
if (isNaN(a)) {
  console.log('1');
} else {
  function factorial (a) {
    if (a > 0) {
      console.log(factorial(a - 1) * a);
    }
  }
console.log(factorial(process.argv[2]));
}
