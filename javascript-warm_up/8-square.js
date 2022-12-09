#!/usr/bin/node
/* Analysis of string that is done in argument */
const b = parseInt(process.argv[2]);
/* if b is not a number, print 'Missin...' */
if (isNaN(b)) {
  console.log('Missing size');
} else {
  let s = '';
  for (let i = 0; i < b; i++) {
    for (let j = 0; j < b; j++) {
      s += '#';
    }
    s += '\n';
  }
  console.log(s);
}
