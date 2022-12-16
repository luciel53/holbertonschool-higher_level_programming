#!/usr/bin/node
/* a JavaScript script that fetches the character name from this URL:
https://swapi-api.hbtn.io/api/people/5/?format=json */
const $ = window.$;
// Fetch the url with get
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
// add the character name to the div#character
  $('DIV#character').append(data.name);
});
