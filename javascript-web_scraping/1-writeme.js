#!/usr/bin/node
/* a script that writes a string to a file. */
const fs = require('fs');
fs.writeFileSync(process.argv[2], process.argv[3]);
