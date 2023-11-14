#!/usr/bin/node
let count = 0;
exports.logic = function (item) { console.log(`${count++}: ${item}`); };
