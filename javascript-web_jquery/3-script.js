#!/usr/bin/node
/* a JavaScript script that updates the text color of the <header> element
to red (#FF0000) */
const $ = window.$;
$('#red_header').click(function () {
  $('header').addClass('red');
});
