#!/usr/bin/node
/* a script that prints the title of a Star Wars movie where the episode
number matches a given integer. */

const request = require('request');
/* url of star wars API + arg that is equal to the id of the episode */
const url = ('https://swapi-api.hbtn.io/api/films/' + process.argv[2]);
request(url, function (error, response, body) {
  /* takes a JSON string and returns a Javascript object */
  body = JSON.parse(body);
  /* prints the title */
  console.log(body.title);
});
