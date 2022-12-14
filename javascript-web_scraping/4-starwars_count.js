#!/usr/bin/node
/* a script that prints the number of movies where the character
“Wedge Antilles” is present. */

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (body === undefined) {
    console.error('error:', error);
  } else {
    /* json to a javascript object */
    const tojavasobj = JSON.parse(body);

    /* count the number of movies (reduce adds) */
    for (let i = 0; tojavasobj.results[i]; i++) {
      if (tojavasobj.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
	console.log(count);
  }

});
